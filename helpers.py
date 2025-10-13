import pandas as pd
import numpy as np
from pymcdm.methods import TOPSIS, VIKOR, WASPAS, MABAC
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm_reidentify.methods import STFN
from pymcdm_reidentify.normalizations import FuzzyNormalization
from PySide6.QtWidgets import QTableWidgetItem, QGraphicsScene, QMessageBox
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

def load_data(app, file_loc):
    data = pd.read_csv(file_loc)
    if data.size == 0:
        return
    app.data = data
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
    return bounds


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
    weights = np.array([0.15, 0.228, 0.222, 0.21, 0.19])
    # weights = app.weights # it will be added later
    stoch = OriginalPSO(epoch=1000, pop_size=int(app.ui.pso_pop_size.text()))
    expert_rank = np.array([int(x.strip()) for x in app.ui.expert_rank.text().split(',')])
    print(f"expert rank: {expert_rank}")
    print(f"data matrix: {app.data_matrix}")
    print(f"bounds: {bounds}")

    stfn = STFN(stoch.solve, TOPSIS(), bounds, weights)
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
        fig, ax = plt.subplots(figsize=(8, 4), dpi=150, tight_layout=True)
        tfn_plot(fun, a, m, b, crit=i, ax=ax)
        canvas = FigureCanvas(fig)
        scene.addWidget(canvas)
        app.ui.stfn_plot.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)
        plt.close(fig)
        app.stfn_plot_index = index

def tfn_plot(tfn,
            a,
            m,
            b,
            crit=None,
            plot_kwargs=dict(),
            text_kwargs=dict(),
            ax=None):

    if ax is None:
        ax = plt.gca()

    plot_kwargs = dict(
        linestyle='-',
        color='black'
    ) | plot_kwargs

    text_kwargs = dict(
        color='black'
    ) | text_kwargs

    width = abs(b - a)
    start = a - width * 0.1
    stop  = b + width * 0.1
    x = np.linspace(start, stop, 150)

    ax.plot(x, tfn(x), **plot_kwargs)

    if crit is not None:
        ax.annotate(f'$C_{crit}^{{core}}$',(m - abs(b - a) * 0.01, 1.05), **text_kwargs)
        ax.set_title(f'$C_{crit}^{{core}}={m:.2f}$')
    else:
        ax.annotate(f'$C^{{core}}$', (m - abs(b - a) * 0.01, 1.05), **text_kwargs)
        ax.set_title(f'$C^{{core}}={m:.2f}$')

    ax.grid(True, linestyle='--', alpha=0.2, color='black')
    ax.set_axisbelow(True)
    ax.set_ylim(0, 1.3)

    ax.set_ylabel(r'$\mu(x)$')
    ax.set_xlabel('x')

    return ax


#? MCDA
def calculate_MCDA(app):
    print("-----------------------------------------")
    print("calculateMCDA")
    app.ui.ranking_new.clear()

    method = app.ui.mcda_method.currentText()
    if app.stfn is None:
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
        body = VIKOR(FuzzyNormalization(app.stfn()))
        print(method)
    elif method == "WASPAS":
        body = WASPAS(FuzzyNormalization(app.stfn()))
        print(method)
    elif method == "MABAC":
        body = MABAC(FuzzyNormalization(app.stfn()))
        print(method)
    
    if body is None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Please choose a valid MCDA method.')
        msg.setWindowTitle("Error")
        msg.exec()
        return

    
    types = np.array([int(x.strip()) for x in app.ui.criteria_types.text().split(',')])
    weights = np.array([float(x.strip()) for x in app.ui.criteria_weights.text().split(',')])

    pref = body(app.data_matrix, weights, types)
    rank = body.rank(pref)
    expert_rank = np.array([int(x.strip()) for x in app.ui.expert_rank.text().split(',')])
    
    app.ui.ranking_new.setPlainText(
        f"{method} result: {rank}\n"
    )

    
    print(f"types: {types}")
    print(f"weights: {weights}")
    print(f"bounds: {app.bounds}")
    print(f"stfn cores: {app.stfn.cores}")
    print("app.data_matrix shape:", app.data_matrix.shape)
    print(len(weights), len(types), len(app.bounds))

    show_mcda_plot_rank(app, expert_rank, rank, method)

def show_mcda_plot_rank(app, expert_rank, rank, method):
    # Clear previous scene if exists
    scene = app.ui.mcda_plot.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.mcda_plot.setScene(scene)
    else:
        scene.clear()

    fig, ax = plt.subplots(figsize=(8, 4), dpi=300, tight_layout=True)
    # Create bar plot with bars next to each other
    x = np.arange(len(rank))
    width = 0.4  # Width of the bars

    bars1 = ax.bar(x - width / 2, expert_rank, width, color='blue', alpha=0.7, label='Expert Rank')
    bars2 = ax.bar(x + width / 2, rank, width, color='orange', alpha=0.7, label='STFN Rank')
    
    ax.set_yticks(range(int(min(expert_rank)), int(max(expert_rank))+2))

    # Add scores above each bar
    ax.bar_label(bars1, fmt='%.2f', padding=3, fontsize=8)
    ax.bar_label(bars2, fmt='%.2f', padding=3, fontsize=8)
    # for i, (e_score, m_score) in enumerate(zip(expert_rank, rank)):
    #     ax.text(i - width / 2, e_score + 0.1, f'{e_score:.2f}', ha='center', va='bottom', fontsize=8)
    #     ax.text(i + width / 2, m_score + 0.1, f'{m_score:.2f}', ha='center', va='bottom', fontsize=8)

    # Add grid to the plot
    ax.grid(True, linestyle='--', alpha=0.7)

    ax.set_xlabel('Alternatives')
    ax.set_ylabel('Rank')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)
    ax.set_title(f'STFN-{method}')
    canvas = FigureCanvas(fig)
    scene.addWidget(canvas)
    app.ui.mcda_plot.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)
    # plt.show()