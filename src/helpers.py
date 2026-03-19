import logging
import re

import numpy as np
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm.methods import MABAC, TOPSIS, VIKOR
from pymcdm_reidentify.methods import STFN
from pymcdm_reidentify.normalizations import FuzzyNormalization
from PySide6.QtCore import QObject, Qt, QThread, Signal
from PySide6.QtWidgets import QTableWidgetItem

import logic
import visualization
import validation
import ui_helpers


class ProgressLogHandler(logging.Handler):
    def __init__(self, signal, max_epochs):
        super().__init__()
        self.signal = signal
        self.max_epochs = max_epochs
        self.epoch_pattern = re.compile(r"Epoch: (\d+)")

    def emit(self, record):
        msg = self.format(record)
        match = self.epoch_pattern.search(msg)
        if match:
            epoch_number = int(match.group(1))
            print(f"DEBUG: epoch {epoch_number} out of {self.max_epochs}")
            self.signal.emit(epoch_number, self.max_epochs)


class STFNWorker(QObject):
    stfn_finished = Signal(object, dict)
    stfn_error = Signal(str)
    stfn_progress = Signal(int, int)

    def __init__(self, stfn, data_matrix, expert_rank, extra_data, max_epochs):
        super().__init__()
        self.stfn = stfn
        self.data_matrix = data_matrix
        self.expert_rank = expert_rank
        self.extra_data = extra_data
        self.max_epochs = max_epochs

    def run(self):
        mealpy_logger = logging.getLogger("mealpy")
        handler = ProgressLogHandler(self.stfn_progress, self.max_epochs)
        mealpy_logger.addHandler(handler)
        mealpy_logger.setLevel(logging.INFO)
        try:
            self.stfn.fit(self.data_matrix, self.expert_rank, log_to="console")
            self.stfn_finished.emit(self.stfn, self.extra_data)
        except Exception as e:
            self.stfn_error.emit(str(e))
        finally:
            mealpy_logger.removeHandler(handler)


np.set_printoptions(suppress=True, precision=4, linewidth=100)


def createDataTable(app, data_frame):
    full_matrix = data_frame.to_numpy()
    field_names = list(data_frame.columns)

    table = app.ui.tbl_data_view
    table.clear()
    table.setRowCount(full_matrix.shape[0])
    table.setColumnCount(full_matrix.shape[1])
    table.verticalHeader().setVisible(False)
    table.setHorizontalHeaderLabels(field_names)

    for row in range(full_matrix.shape[0]):
        for col in range(full_matrix.shape[1]):
            item = QTableWidgetItem(str(full_matrix[row][col]))
            item.setTextAlignment(
                Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
            )
            table.setItem(row, col, item)

    header = table.horizontalHeader()
    header.setSectionResizeMode(header.ResizeMode.Stretch)
    header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap)

    table.executeDelayedItemsLayout()

    padding = 10
    max_height = 20
    for i in range(table.columnCount()):
        current_width = header.sectionSize(i)
        text = table.horizontalHeaderItem(i).text()
        rect = header.fontMetrics().boundingRect(
            0,
            0,
            current_width - 10,
            1000,
            Qt.TextFlag.TextWordWrap | Qt.AlignmentFlag.AlignCenter,
            text,
        )
        col_height = rect.height()
        if col_height > max_height:
            max_height = col_height

    header.setFixedHeight(max_height + padding)
    table.setWordWrap(True)
    table.setAlternatingRowColors(True)
    table.resizeRowsToContents()


def on_stfn_calculated(app, stfn, expert_rank_txt, weights_txt, method):
    ui_helpers.enable_all_buttons(app)

    cores_formatted = ", ".join([f"{core:.4f}" for core in stfn.cores])
    app.ui.txt_stfn_results.setPlainText(f"STFN cores: {cores_formatted}")

    app.ui.txt_old_ranking.setPlainText(expert_rank_txt)
    app.ui.txt_weights_mcda.setPlainText(weights_txt)
    app.ui.txt_mcda_method.setPlainText(method)

    for i, (fun, a, m, b) in enumerate(zip(stfn(), stfn.lb, stfn.cores, stfn.ub), 1):
        app.stfn_plot_data.append((fun, a, m, b, i))
    visualization.show_stfn_plot(app, 0)


def on_stfn_error(app, error_message):
    ui_helpers.showErrorMessage("STFN Calculation Error", error_message)
    ui_helpers.enable_all_buttons(app)


def set_stfn_to_background(app, stfn, expert_rank, data, max_epochs):
    app.thread = QThread()
    app.worker = STFNWorker(stfn, app.data_matrix, expert_rank, data, max_epochs)
    app.worker.moveToThread(app.thread)

    app.worker.stfn_finished.connect(app.success_handler, type=Qt.QueuedConnection)
    app.worker.stfn_error.connect(app.error_handler, type=Qt.QueuedConnection)

    app.worker.stfn_progress.connect(app.progress_handler)

    app.thread.started.connect(app.worker.run)

    app.worker.stfn_finished.connect(app.thread.quit)
    app.worker.stfn_error.connect(app.thread.quit)
    app.worker.stfn_finished.connect(app.worker.deleteLater)
    app.worker.stfn_error.connect(app.worker.deleteLater)
    app.thread.finished.connect(app.thread.deleteLater)

    app.thread.start()


def calculate_STFN(app):
    if app.data_matrix is None:
        ui_helpers.showErrorMessage("Error", "Please import data first.")
        return

    app.ui.txt_stfn_results.clear()
    app.stfn_plot_data = []
    app.stfn_plot_index = 0

    bounds_text = app.ui.txt_bounds_data.toPlainText().strip()
    if bounds_text:
        app.bounds = logic.parse_bounds_from_text(bounds_text)
    bounds = app.bounds

    weights_txt = app.ui.txt_criteria_weights.toPlainText()
    weights = np.array([float(x.strip()) for x in weights_txt.split(",")])
    app.weights = weights
    max_epochs = int(app.ui.txt_epoch_size.toPlainText())
    pop_size = int(app.ui.txt_population_size.toPlainText())
    c1 = float(app.ui.txt_c1_size.toPlainText())
    c2 = float(app.ui.txt_c2_size.toPlainText())
    w = float(app.ui.txt_w_size.toPlainText())
    expert_rank_txt = app.ui.txt_alternatives_ranking.toPlainText()
    expert_rank = np.array([int(x.strip()) for x in expert_rank_txt.split(",")])
    app.expert_rank = expert_rank

    if not validation.checkIfSTFNReady(app):
        ui_helpers.showErrorMessage(
            "Error", "Make sure data, bounds, weights, and expert rank are set."
        )
        return

    if not validation.checkIfPSOReady(pop_size, max_epochs, c1, c2, w):
        ui_helpers.showErrorMessage("Error", "Make sure PSO parameters are valid.")
        return

    ui_helpers.disable_all_buttons(app)

    ui_helpers.clear_or_set_scene(app.ui.gv_stfn_visualization)

    method = app.ui.cb_mcda_method.currentText()
    app.mcda_method = method

    app.ui.progressBar.setRange(0, 100)
    app.ui.progressBar.setValue(0)

    stoch = OriginalPSO(epoch=max_epochs, pop_size=pop_size, c1=c1, c2=c2, w=w)

    if method == "TOPSIS":
        stfn = STFN(stoch.solve, TOPSIS(), bounds, weights)
    elif method == "VIKOR":
        stfn = STFN(stoch.solve, VIKOR(), bounds, weights)
    elif method == "MABAC":
        stfn = STFN(stoch.solve, MABAC(), bounds, weights)
    else:
        ui_helpers.showErrorMessage("Error", "Make sure valid MCDA method is selected.")
        ui_helpers.enable_all_buttons(app)
        return

    data = {
        "expert_rank_txt": expert_rank_txt,
        "weights_txt": weights_txt,
        "method": method,
    }

    set_stfn_to_background(app, stfn, expert_rank, data, max_epochs)


def calculate_MCDA(app):
    app.ui.txt_new_ranking.clear()
    if app.stfn is None:
        ui_helpers.showErrorMessage("Error", "Please run STFN first.")
        return
    body = None

    method = app.mcda_method

    if not validation.checkIfMCDAReady(app):
        ui_helpers.showErrorMessage(
            "Error", "Please make sure STFN is calculated and MCDA method is selected."
        )
        return

    ob_norm = FuzzyNormalization(app.stfn())

    if method == "TOPSIS":
        body = TOPSIS(ob_norm)
    elif method == "VIKOR":
        body = VIKOR(ob_norm)
    elif method == "MABAC":
        body = MABAC(ob_norm)

    if body is None:
        ui_helpers.showErrorMessage("Error", "Please choose a valid MCDA method.")
        return

    types = np.ones(app.data_matrix.shape[1])
    weights = app.weights

    pref = body(app.data_matrix, weights, types)
    app.stfn_mcda_body = body
    rank = body.rank(pref)
    expert_rank = app.expert_rank

    new_rank_txt = np.array2string(rank.astype(int), separator=", ")[1:-1]

    app.new_rank = rank
    app.ui.txt_new_ranking.setPlainText(new_rank_txt)

    visualization.show_mcda_rank_plot(app, expert_rank, rank, method)
    visualization.show_mcda_corelation_plot(app, expert_rank, rank, method)
