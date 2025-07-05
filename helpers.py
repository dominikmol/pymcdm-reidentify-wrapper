import pandas as pd
import numpy as np
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm_reidentify.methods import STFN
from pymcdm.methods import TOPSIS
from PySide6.QtWidgets import QTableWidgetItem


def make_bounds(matrix):
    bounds = np.array([[np.min(matrix[:, i]), np.max(matrix[:, i])]
                      for i in range(matrix.shape[1])])
    return bounds


def loadData(app, file_loc):
    data = pd.read_csv(file_loc)
    if data.size == 0:
        return
    app.data_matrix = data.iloc[:, 1:].to_numpy()
    matrix = data.to_numpy()
    fieldnames = list(data.columns)
    
    # print("Full matrix:")
    # print(matrix)
    # print("Field names:")
    # print(fieldnames)
    # print("Data matrix (numeric only):")
    # print(app.data_matrix)

    table = app.ui.data_table
    table.clear()  # Clear existing content
    table.setRowCount(matrix.shape[0])
    table.setColumnCount(matrix.shape[1])
    table.setHorizontalHeaderLabels(fieldnames)

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            item = QTableWidgetItem(str(matrix[row][col]))
            table.setItem(row, col, item)


def calculateSTFN(app):
    print("-----------------------------------------")
    print("calculateSTFN")
    app.ui.stfn_results.clear()
    criteria_types = [int(x.strip()) for x in app.ui.criteria_types.text().split(',')]
    bounds = app.bounds
    stoch = OriginalPSO(epoch=1000, pop_size=int(app.ui.pso_pop_size.text()))
    expert_rank = np.array([int(x.strip()) for x in app.ui.expert_rank.text().split(',')])
    # expert_rank = [int(x.strip()) for x in app.ui.expert_rank.text().split(',')] # [3, 1, 9, 10, 5, 7, 2, 6, 8, 4]
    print(f"expert rank: {expert_rank}")
    print(f"data matrix: {app.data_matrix}")

    print(f"bounds: {bounds}")
    print(f"types: {criteria_types}")

    stfn = STFN(stoch.solve, TOPSIS(), bounds)
    stfn.fit(app.data_matrix, expert_rank, log_to=None)
    print(f"cores: {stfn.cores}")
    app.ui.stfn_results.setPlainText(
        f"STFN cores: {stfn.cores}")