import pandas as pd
import numpy as np
from pymcdm.methods import TOPSIS
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm_reidentify.methods import STFN
from pymcdm_reidentify.normalizations import FuzzyNormalization
from pymcdm_reidentify.visuals import model_contourf, tfn_plot
from PySide6.QtWidgets import QTableWidgetItem, QGraphicsScene
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure


def make_bounds(matrix):
    bounds = np.array([[np.min(matrix[:, i]), np.max(matrix[:, i])]
                      for i in range(matrix.shape[1])])
    return bounds.tolist()


def loadData(app, file_loc):
    data = pd.read_csv(file_loc)
    if data.size == 0:
        return
    app.data_matrix = data.iloc[:, 1:].to_numpy()
    matrix = data.to_numpy()
    fieldnames = list(data.columns)

    table = app.ui.data_table
    table.clear()
    table.setRowCount(matrix.shape[0])
    table.setColumnCount(matrix.shape[1])
    table.setHorizontalHeaderLabels(fieldnames)

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            item = QTableWidgetItem(str(matrix[row][col]))
            table.setItem(row, col, item)


def calculate_STFN(app):
    print("-----------------------------------------")
    print("calculateSTFN")
    app.ui.stfn_results.clear()
    app.stfn_plot_data = []
    app.stfn_plot_index = 0

    bounds = app.bounds
    stoch = OriginalPSO(epoch=1000, pop_size=int(app.ui.pso_pop_size.text()))
    expert_rank = np.array([int(x.strip()) for x in app.ui.expert_rank.text().split(',')])
    print(f"expert rank: {expert_rank}")
    print(f"data matrix: {app.data_matrix}")
    print(f"bounds: {bounds}")

    stfn = STFN(stoch.solve, TOPSIS(), bounds)
    stfn.fit(app.data_matrix, expert_rank, log_to=None)
    app.stfn = stfn
    print(f"cores: {stfn.cores}")
    
    app.ui.stfn_results.setPlainText(f"STFN cores: {stfn.cores}")
    app.ui.ranking_new.setPlainText(f"STFN cores: {stfn.cores}")

    for i, (fun, a, m, b) in enumerate(zip(stfn(), stfn.lb, stfn.cores, stfn.ub), 1):
        app.stfn_plot_data.append((fun, a, m, b, i))
    show_stfn_plot(app, 0)

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

