from pymcdm.methods import TOPSIS, VIKOR, WASPAS, MABAC
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm_reidentify.methods import STFN
from pymcdm_reidentify.normalizations import FuzzyNormalization
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
import numpy as np
import logic
import visualization


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

    # table = app.ui.data_table
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

def calculate_STFN(app):
    if app.data_matrix is None:
        showErrorMessage(
            "Error",
            'Please import data first.'
            )
        return

    # print("-----------------------------------------")
    # print("calculateSTFN")
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

    stoch = OriginalPSO(epoch=epoch, pop_size=pop_size, c1=c1, c2=c2, w=w)
    # print(f"expert rank: {expert_rank}")
    # print(f"data matrix: {app.data_matrix}")
    # print(f"bounds: {bounds}")

    method = app.ui.cb_mcda_method.currentText()
    app.mcda_method = method

    if method == "TOPSIS":
        # print(method)
        stfn = STFN(stoch.solve, TOPSIS(), bounds, weights)
    elif method == "VIKOR":
        stfn = STFN(stoch.solve, VIKOR(), bounds, weights)
        # print(method)
    elif method == "WASPAS":
        stfn = STFN(stoch.solve, WASPAS(), bounds, weights)
        # print(method)
    elif method == "MABAC":
        stfn = STFN(stoch.solve, MABAC(), bounds, weights)
        # print(method)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Make sure MCDA method is selected.')
        msg.setWindowTitle("Error")
        msg.exec()
        return

    # stfn = STFN(stoch.solve, TOPSIS(), bounds, weights)
    stfn.fit(app.data_matrix, expert_rank, log_to=None)
    app.stfn = stfn
    # print(f"cores: {stfn.cores}")

    cores_formatted = ", ".join([f"{core:.4f}" for core in stfn.cores])
    app.ui.txt_stfn_results.setPlainText(f"STFN cores: {cores_formatted}")

    # text_expert_rank
    app.ui.txt_old_ranking.setPlainText(expert_rank_txt)
    app.ui.txt_weights_mcda.setPlainText(weights_txt)
    app.ui.txt_mcda_method.setPlainText(method)

    for i, (fun, a, m, b) in enumerate(zip(stfn(), stfn.lb, stfn.cores, stfn.ub), 1):
        app.stfn_plot_data.append((fun, a, m, b, i))
    visualization.show_stfn_plot(app, 0)


def calculate_MCDA(app):
    # print("-----------------------------------------")
    # print("calculateMCDA")
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
        # print(method)
        body = TOPSIS(ob_norm)
    elif method == "VIKOR":
        body = VIKOR(ob_norm)
        # print(method)
    elif method == "WASPAS":
        body = WASPAS(ob_norm)
        # print(method)
    elif method == "MABAC":
        body = MABAC(ob_norm)
        # print(method)
    
    if body is None:
        showErrorMessage(
            "Error",
            'Please choose a valid MCDA method.'
            )
        return

    
    types = np.ones(app.data_matrix.shape[1])
    # print(f"MCDA TYPES: {types}")
    weights = app.weights
    # print(f"MCDA weights: {weights}")

    pref = body(app.data_matrix, weights, types)
    rank = body.rank(pref)
    expert_rank = app.expert_rank
    
    # print(f"expert_rank : {expert_rank}")
    # print(f"new rank: {rank}")

    new_rank_txt = np.array2string(rank.astype(int), separator=', ')[1:-1]

    app.new_rank = rank
    app.ui.txt_new_ranking.setPlainText(new_rank_txt)

    
    # print(f"types: {types}")
    # print(f"weights: {weights}")
    # print(f"bounds: {app.bounds}")
    # print(f"stfn cores: {app.stfn.cores}")
    # print("app.data_matrix shape:", app.data_matrix.shape)
    # print(len(weights), len(types), len(app.bounds))

    visualization.show_mcda_rank_plot(app, expert_rank, rank, method)
    visualization.show_mcda_corelation_plot(app, expert_rank, rank, method)
