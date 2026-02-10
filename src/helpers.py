from pymcdm.methods import TOPSIS, VIKOR, WASPAS, MABAC
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm_reidentify.methods import STFN
from pymcdm_reidentify.normalizations import FuzzyNormalization
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
import numpy as np
import logic
import visualization
from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtCore import Qt


class STFNWorker(QObject):
    stfn_finished = Signal(object, dict)
    stfn_error = Signal(str)

    def __init__(self, stfn, data_matrix, expert_rank, extra_data):
        super().__init__()
        self.stfn = stfn
        self.data_matrix = data_matrix
        self.expert_rank = expert_rank
        self.extra_data = extra_data

    def run(self):
        try:
            self.stfn.fit(self.data_matrix, self.expert_rank)
            self.stfn_finished.emit(self.stfn, self.extra_data)
        except Exception as e:
            self.stfn_error.emit(str(e))


np.set_printoptions(suppress=True, precision=4, linewidth=100)

def showErrorMessage(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(title)
    msg.setInformativeText(message)
    msg.setWindowTitle("Error")
    msg.exec()

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
            table.setItem(row, col, item)

def checkIfSTFNReady(app):
    if app.data_matrix is None:
        return False
    if app.bounds is None:
        return False
    if app.weights is None:
        return False
    if app.expert_rank is None:
        return False
    return True

def checkIfPSOReady(pop_size, epoch, c1, c2, w):
    if pop_size <= 0 or epoch <= 0:
        return False
    if not (0 < c1 < 4) or not (0 < c2 < 4) or not (0 < w < 1):
        return False
    return True

def checkIfMCDAReady(app):
    if app.stfn is None:
        return False
    if app.mcda_method is None:
        return False
    return True

def disable_all_buttons(app):
    app.ui.btn_load_data.setEnabled(False)
    app.ui.btn_generate_bounds.setEnabled(False)
    app.ui.btn_calculate_stfn.setEnabled(False)
    app.ui.btn_calculate_ranking.setEnabled(False)
    app.ui.btn_previous_visualization.setEnabled(False)
    app.ui.btn_next_visualization.setEnabled(False)


def enable_all_buttons(app):
    app.ui.btn_load_data.setEnabled(True)
    app.ui.btn_generate_bounds.setEnabled(True)
    app.ui.btn_calculate_stfn.setEnabled(True)
    app.ui.btn_calculate_ranking.setEnabled(True)
    app.ui.btn_previous_visualization.setEnabled(True)
    app.ui.btn_next_visualization.setEnabled(True) 

def on_stfn_calculated(app, stfn, expert_rank_txt, weights_txt, method):
    print("DEBUG: Rozpoczynam on_stfn_calculated")
    enable_all_buttons(app)
    
    cores_formatted = ", ".join([f"{core:.4f}" for core in stfn.cores])
    app.ui.txt_stfn_results.setPlainText(f"STFN cores: {cores_formatted}")

    app.ui.txt_old_ranking.setPlainText(expert_rank_txt)
    app.ui.txt_weights_mcda.setPlainText(weights_txt)
    app.ui.txt_mcda_method.setPlainText(method)

    for i, (fun, a, m, b) in enumerate(zip(stfn(), stfn.lb, stfn.cores, stfn.ub), 1):
        app.stfn_plot_data.append((fun, a, m, b, i))
    visualization.show_stfn_plot(app, 0)

def on_stfn_error(app, error_message):
    showErrorMessage("STFN Calculation Error", error_message)
    enable_all_buttons(app)

# def handle_finished(app, stfn, data):
#     app.stfn = stfn
#     on_stfn_calculated(app, stfn, **data)

def set_stfn_to_background(app, stfn, expert_rank, data):
    app.thread = QThread()
    app.worker = STFNWorker(stfn, app.data_matrix, expert_rank, data)
    app.worker.moveToThread(app.thread)

    app.worker.stfn_finished.connect(
        app.success_handler,
        type=Qt.QueuedConnection
        )
    app.worker.stfn_error.connect(
        app.error_handler,
        type=Qt.QueuedConnection
        )

    app.thread.started.connect(app.worker.run)

    app.worker.stfn_finished.connect(app.thread.quit)
    app.worker.stfn_error.connect(app.thread.quit)
    app.worker.stfn_finished.connect(app.worker.deleteLater)
    app.worker.stfn_error.connect(app.worker.deleteLater)
    app.thread.finished.connect(app.thread.deleteLater)

    app.thread.start()



def calculate_STFN(app):
    if app.data_matrix is None:
        showErrorMessage(
            "Error",
            'Please import data first.'
            )
        return

    app.ui.txt_stfn_results.clear()
    app.stfn_plot_data = []
    app.stfn_plot_index = 0
    
    bounds_text = app.ui.txt_bounds_data.toPlainText().strip()
    if bounds_text:
        app.bounds = logic.parse_bounds_from_text(bounds_text)
    bounds = app.bounds
    
    weights_txt = app.ui.txt_criteria_weights.toPlainText()
    weights = np.array([float(x.strip()) for x in weights_txt.split(',')])
    app.weights = weights
    epoch = int(app.ui.txt_epoch_size.toPlainText())
    pop_size = int(app.ui.txt_population_size.toPlainText())
    c1 = float(app.ui.txt_c1_size.toPlainText())
    c2 = float(app.ui.txt_c2_size.toPlainText())
    w = float(app.ui.txt_w_size.toPlainText())
    expert_rank_txt = app.ui.txt_alternatives_ranking.toPlainText()
    expert_rank = np.array([int(x.strip()) for x in expert_rank_txt.split(',')])
    app.expert_rank = expert_rank

    if not checkIfSTFNReady(app):
        showErrorMessage(
            "Error",
            'Make sure data, bounds, weights, and expert rank are set.'
            )
        return

    if not checkIfPSOReady(pop_size, epoch, c1, c2, w):
        showErrorMessage(
            "Error",
            'Make sure PSO parameters are valid.'
            )
        return

    app.ui.txt_stfn_results.setPlainText("WORKING!!!!!!!!!!!")

    disable_all_buttons(app)

    method = app.ui.cb_mcda_method.currentText()
    app.mcda_method = method

    stoch = OriginalPSO(epoch=epoch, pop_size=pop_size, c1=c1, c2=c2, w=w)

    if method == "TOPSIS":
        stfn = STFN(stoch.solve, TOPSIS(), bounds, weights)
    elif method == "VIKOR":
        stfn = STFN(stoch.solve, VIKOR(), bounds, weights)
    elif method == "WASPAS":
        stfn = STFN(stoch.solve, WASPAS(), bounds, weights)
    elif method == "MABAC":
        stfn = STFN(stoch.solve, MABAC(), bounds, weights)
    else:
        showErrorMessage(
            "Error",
            'Make sure valid MCDA method is selected.'
        )
        enable_all_buttons(app)
        return

    data = {
        'expert_rank_txt': expert_rank_txt,
        'weights_txt': weights_txt,
        'method': method
        }

    set_stfn_to_background(app, stfn, expert_rank, data)


def calculate_MCDA(app):
    app.ui.txt_new_ranking.clear()
    if app.stfn is None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Please run STFN first.')
        msg.setWindowTitle("Error")
        msg.exec()
        return
    body = None

    method = app.mcda_method

    if not checkIfMCDAReady(app):
        showErrorMessage(
            "Error",
            'Please make sure STFN is calculated and MCDA method is selected.'
            )
        return

    ob_norm = FuzzyNormalization(app.stfn())

    if method == "TOPSIS":
        body = TOPSIS(ob_norm)
    elif method == "VIKOR":
        body = VIKOR(ob_norm)
    elif method == "WASPAS":
        body = WASPAS(ob_norm)
    elif method == "MABAC":
        body = MABAC(ob_norm)
    
    if body is None:
        showErrorMessage(
            "Error",
            'Please choose a valid MCDA method.'
            )
        return

    
    types = np.ones(app.data_matrix.shape[1])
    weights = app.weights

    pref = body(app.data_matrix, weights, types)
    rank = body.rank(pref)
    expert_rank = app.expert_rank

    new_rank_txt = np.array2string(rank.astype(int), separator=', ')[1:-1]

    app.new_rank = rank
    app.ui.txt_new_ranking.setPlainText(new_rank_txt)

    visualization.show_mcda_rank_plot(app, expert_rank, rank, method)
    visualization.show_mcda_corelation_plot(app, expert_rank, rank, method)
