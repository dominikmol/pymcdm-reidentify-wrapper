import numpy as np
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm.methods import MABAC, TOPSIS, VIKOR
from pymcdm_reidentify.methods import STFN
from pymcdm_reidentify.normalizations import FuzzyNormalization
from PySide6.QtCore import Qt, QThread

import logic
import visualization
import validation
import ui_helpers
import stfn_worker


np.set_printoptions(suppress=True, precision=4, linewidth=100)

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

    ob_norm = FuzzyNormalization(stfn())
    stfn_methods = {
        "TOPSIS": TOPSIS(ob_norm),
        "VIKOR": VIKOR(ob_norm),
        "MABAC": MABAC(ob_norm),
    }
    app.stfn_mcda_body = stfn_methods.get(method)


def on_stfn_error(app, error_message):
    ui_helpers.showErrorMessage("STFN Calculation Error", error_message)
    ui_helpers.enable_all_buttons(app)


def set_stfn_to_background(app, stfn, expert_rank, data, max_epochs):
    app.thread = QThread()
    app.worker = stfn_worker.STFNWorker(stfn, app.data_matrix, expert_rank, data, max_epochs)
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
    stfn_methods = {
        "TOPSIS": TOPSIS(),
        "VIKOR": VIKOR(),
        "MABAC": MABAC(),
    }

    if method not in stfn_methods:
        ui_helpers.showErrorMessage("Error", "Make sure valid MCDA method is selected.")
        ui_helpers.enable_all_buttons(app)
        return

    stfn = STFN(stoch.solve, stfn_methods[method], bounds, weights)

    data = {
        "expert_rank_txt": expert_rank_txt,
        "weights_txt": weights_txt,
        "method": method,
    }

    set_stfn_to_background(app, stfn, expert_rank, data, max_epochs)


def calculate_MCDA(app):
    app.ui.txt_new_ranking.clear()    

    if not validation.checkIfMCDAReady(app):
        ui_helpers.showErrorMessage(
            "Error", "Please make sure STFN is calculated and MCDA method is selected."
        )
        return

    method = app.mcda_method

    body = app.stfn_mcda_body
    types = np.ones(app.data_matrix.shape[1])
    weights = app.weights

    pref = body(app.data_matrix, weights, types)
    rank = body.rank(pref)
    expert_rank = app.expert_rank

    new_rank_txt = np.array2string(rank.astype(int), separator=", ")[1:-1]

    app.new_rank = rank
    app.ui.txt_new_ranking.setPlainText(new_rank_txt)

    visualization.show_mcda_rank_plot(app, expert_rank, rank, method)
    visualization.show_mcda_corelation_plot(app, expert_rank, rank, method)