import pandas as pd
import numpy as np
from pymcdm.methods import TOPSIS
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm_reidentify.methods import STFN
from pymcdm_reidentify.normalizations import FuzzyNormalization
from pymcdm_reidentify.visuals import model_contourf, tfn_plot
from PySide6.QtWidgets import QTableWidgetItem, QGraphicsScene, QMessageBox
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure

def load_data(app, file_loc):
    data = pd.read_csv(file_loc)
    if data.size == 0:
        return
    app.data_matrix = data.iloc[:, 1:].to_numpy()
    full_matrix = data.to_numpy()
    field_names = list(data.columns)

    table = app.ui.data_table
    table.clear()
    table.setRowCount(full_matrix.shape[0])
    table.setColumnCount(full_matrix.shape[1])
    table.setHorizontalHeaderLabels(field_names)

    for row in range(full_matrix.shape[0]):
        for col in range(full_matrix.shape[1]):
            item = QTableWidgetItem(str(full_matrix[row][col]))
            table.setItem(row, col, item)
            

def make_bounds(data_matrix):
    bounds = np.array([[np.min(data_matrix[:, i]), np.max(data_matrix[:, i])]
                      for i in range(data_matrix.shape[1])])
    return bounds #.tolist()


#? STFN
def calculate_STFN(app):
    if app.data_matrix is None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Please import data first.')
        msg.setWindowTitle("Error")
        msg.exec()
        return

    print("-----------------------------------------")
    print("calculateSTFN")
    app.ui.stfn_results.clear()
    app.stfn_plot_data = []
    app.stfn_plot_index = 0

    bounds = app.bounds
    we = np.array([0.15, 0.228, 0.222, 0.21, 0.19])
    stoch = OriginalPSO(epoch=1000, pop_size=int(app.ui.pso_pop_size.text()))
    expert_rank = np.array([int(x.strip()) for x in app.ui.expert_rank.text().split(',')])
    print(f"expert rank: {expert_rank}")
    print(f"data matrix: {app.data_matrix}")
    print(f"bounds: {bounds}")

    stfn = STFN(stoch.solve, TOPSIS(), bounds, we)
    stfn.fit(app.data_matrix, expert_rank, log_to=None)
    app.stfn = stfn
    print(f"cores: {stfn.cores}")
    
    app.ui.stfn_results.setPlainText(f"STFN cores: {stfn.cores}")
    app.ui.ranking_new.setPlainText(f"STFN cores: {stfn.cores}")

    for i, (fun, a, m, b) in enumerate(zip(stfn(), stfn.lb, stfn.cores, stfn.ub), 1):
        app.stfn_plot_data.append((fun, a, m, b, i))
    show_stfn_plot(app, 0)


#? STFN plot
def show_stfn_plot(app, index):
    # Clear previous scene if exists
    scene = app.ui.stfn_plot.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.stfn_plot.setScene(scene)
    else:
        scene.clear()
    
    if 0 <= index < len(app.stfn_plot_data):
        fun, a, m, b, i = app.stfn_plot_data[index]
        fig, ax = plt.subplots(figsize=(4.5, 2.2), dpi=150, tight_layout=True)
        tfn_plot(fun, a, m, b, crit=i, ax=ax)
        canvas = FigureCanvas(fig)
        scene.addWidget(canvas)
        app.ui.stfn_plot.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)
        app.stfn_plot_index = index


#? MCDA
def calculate_MCDA(app):
    print("-----------------------------------------")
    print("calculateMCDA")
    app.ui.ranking_new.clear()

    method = app.ui.mcda_method.currentText()
    if app.stfn is None:
        # app.ui.ranking_new.setPlainText("Please run STFN first.")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Please run STFN first.')
        msg.setWindowTitle("Error")
        msg.exec()
        return
    body = None

    if method == "TOPSIS":
        print(method)
        body = TOPSIS(FuzzyNormalization(app.stfn()))
    elif method == "VIKOR":
        from pymcdm.methods import VIKOR
        print(method)
        return
        # body = VIKOR(FuzzyNormalization(app.stfn()))
    elif method == "WASPAS":
        from pymcdm.methods import WASPAS
        print(method)
        return
        # body = WAPAS(FuzzyNormalization(app.stfn()))
    
    app.ui.ranking_new.setPlainText(
        f"STFN cores: {app.stfn.cores}\n"
        f"{method} result: {body.rank}\n"
    )

    types = np.array([int(x.strip()) for x in app.ui.criteria_types.text().split(',')])
    weights = np.array([float(x.strip()) for x in app.ui.criteria_weights.text().split(',')])
    print(f"types: {types}")
    print(f"weights: {weights}")
    print(f"bounds: {app.bounds}")
    print(f"stfn cores: {app.stfn.cores}")
    print("app.data_matrix shape:", app.data_matrix.shape)
    print(len(weights), len(types), len(app.bounds))

    show_mcda_plot(app, body, weights, types, method)


#? MCDA plot
def show_mcda_plot(app, body, weights, types, method):
    # Clear previous scene if exists
    scene = app.ui.mcda_plot.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.mcda_plot.setScene(scene)
    else:
        scene.clear()

    #! NOT WORKING
    fig, ax = plt.subplots(figsize=(3, 3),  dpi=150, tight_layout=True)
    model_contourf(
        body, 
        app.bounds, 
        esp=app.stfn.cores, 
        model_kwargs={'weights': weights, 'types': types}, 
        text_kwargs={'text': '$TFNs_{Cores}$'},
        ax = ax)
    ax.set_title(f'STFN-{method}')
    # canvas = FigureCanvas(fig)
    # scene.addWidget(canvas)
    # app.ui.mcda_plot.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)
    plt.show()