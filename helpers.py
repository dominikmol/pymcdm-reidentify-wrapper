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
            

def make_bounds(data_matrix):
    bounds = np.array([[np.min(data_matrix[:, i]), np.max(data_matrix[:, i])]
                      for i in range(data_matrix.shape[1])])
    return bounds

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

def show_stfn_plot(app, index):
    # Clear previous scene if exists
    scene = app.ui.gv_stfn_visualization.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.gv_stfn_visualization.setScene(scene)
    else:
        scene.clear()
    
    if 0 <= index < len(app.stfn_plot_data):
        fun, a, m, b, i = app.stfn_plot_data[index]
        fig, ax = plt.subplots(figsize=(8, 4), dpi=150, tight_layout=True)
        tfn_plot(fun, a, m, b, crit=i, ax=ax)
        canvas = FigureCanvas(fig)
        scene.addWidget(canvas)
        app.ui.gv_stfn_visualization.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)
        plt.close(fig)
        app.stfn_plot_index = index

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
    app.ui.txt_stfn_results.clear()
    app.stfn_plot_data = []
    app.stfn_plot_index = 0
    
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

    stoch = OriginalPSO(epoch=epoch, pop_size=pop_size, c1=c1, c2=c2, w=w)
    print(f"expert rank: {expert_rank}")
    print(f"data matrix: {app.data_matrix}")
    print(f"bounds: {bounds}")

    method = app.ui.cb_mcda_method.currentText()
    app.mcda_method = method

    if method == "TOPSIS":
        print(method)
        stfn = STFN(stoch.solve, TOPSIS(), bounds, weights)
    elif method == "VIKOR":
        stfn = STFN(stoch.solve, VIKOR(), bounds, weights)
        print(method)
    elif method == "WASPAS":
        stfn = STFN(stoch.solve, WASPAS(), bounds, weights)
        print(method)
    elif method == "MABAC":
        stfn = STFN(stoch.solve, MABAC(), bounds, weights)
        print(method)
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
    print(f"cores: {stfn.cores}")
    
    app.ui.txt_stfn_results.setPlainText(f"STFN cores: {stfn.cores}")

    # text_expert_rank
    app.ui.txt_old_ranking.setPlainText(expert_rank_txt)
    app.ui.txt_weights_mcda.setPlainText(weights_txt)
    app.ui.txt_mcda_method.setPlainText(method)

    for i, (fun, a, m, b) in enumerate(zip(stfn(), stfn.lb, stfn.cores, stfn.ub), 1):
        app.stfn_plot_data.append((fun, a, m, b, i))
    show_stfn_plot(app, 0)


def show_mcda_rank_plot(app, expert_rank, rank, method):
    # Clear previous scene if exists
    scene = app.ui.gv_mcda_visualization.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.gv_mcda_visualization.setScene(scene)
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

    # Add grid to the plot
    ax.grid(True, linestyle='--', alpha=0.7)

    ax.set_xlabel('Alternatives')
    ax.set_ylabel('Rank')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)
    ax.set_title(f'STFN-{method}')
    canvas = FigureCanvas(fig)
    scene.addWidget(canvas)
    app.ui.gv_mcda_visualization.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)
    # plt.show()

def rw(rankx, ranky, n):
    suma = 0
    for i in range(n):
        suma += ((
            (rankx[i]-ranky[i])**2)
            *((n-rankx[i]+1)+(n-ranky[i]+1)
                    ))
    suma = 6 * suma
    denominator = n**4 + n**3 - n**2 - n
    if denominator == 0:
        return 0
    suma = suma / denominator
    return 1-suma

def WS(rankx, ranky, n):
    suma = 0
    for i in range(n):
        eq = 2 ** (-float(rankx[i]))
        eq2 = abs(rankx[i] - ranky[i]) / max(abs(1 - rankx[i]), abs(n - rankx[i]))
        suma += eq * eq2
    return 1 - suma

def show_mcda_corelation_plot(app, expert_rank, rank, method):
    # Clear previous scene if exists
    scene = app.ui.gv_correlation_visualization.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.gv_correlation_visualization.setScene(scene)
    else:
        scene.clear()

    fig, ax = plt.subplots(figsize=(8, 4), dpi=300, tight_layout=True)
    # Create bar plot with bars next to each other
    x = np.arange(len(rank))
    ax.scatter(expert_rank, rank, color='black')
    ax.grid(True, linestyle=':')
    ax.set_xlabel("expert rank")
    ax.set_ylabel(f"{method} rank")
    n = len(rank)
    ax.set_title(
        f"rw = {rw(expert_rank, rank, n):.5f}\n WS = {WS(expert_rank, rank, n):.5f}"
        )
    canvas = FigureCanvas(fig)
    scene.addWidget(canvas)
    app.ui.gv_correlation_visualization.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)
    # plt.show()

def calculate_MCDA(app):
    print("-----------------------------------------")
    print("calculateMCDA")
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
    ob_norm = FuzzyNormalization(app.stfn())

    if method == "TOPSIS":
        print(method)
        body = TOPSIS(ob_norm)
    elif method == "VIKOR":
        body = VIKOR(ob_norm)
        print(method)
    elif method == "WASPAS":
        body = WASPAS(ob_norm)
        print(method)
    elif method == "MABAC":
        body = MABAC(ob_norm)
        print(method)
    
    if body is None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Please choose a valid MCDA method.')
        msg.setWindowTitle("Error")
        msg.exec()
        return

    
    # types = np.array([int(x.strip()) for x in app.ui.txt_criteria_types.toPlainText().split(',')])
    types = np.ones(app.data_matrix.shape[1])
    print(f"MCDA TYPES: {types}")
    weights = app.weights
    print(f"MCDA weights: {weights}")
    # weights = np.array([float(x.strip()) for x in app.ui.txt_criteria_weights.toPlainText().split(',')])

    pref = body(app.data_matrix, weights, types)
    rank = body.rank(pref)
    expert_rank = app.expert_rank
    # expert_rank = np.array([int(x.strip()) for x in app.ui.txt_alternatives_ranking.toPlainText().split(',')])
    
    print(f"expert_rank : {expert_rank}")
    print(f"new rank: {rank}")

    new_rank_txt = np.array2string(rank, separator=', ')[1:-1]

    app.new_rank = rank
    app.ui.txt_new_ranking.setPlainText(new_rank_txt)

    
    print(f"types: {types}")
    print(f"weights: {weights}")
    print(f"bounds: {app.bounds}")
    print(f"stfn cores: {app.stfn.cores}")
    print("app.data_matrix shape:", app.data_matrix.shape)
    print(len(weights), len(types), len(app.bounds))

    show_mcda_rank_plot(app, expert_rank, rank, method)
    show_mcda_corelation_plot(app, expert_rank, rank, method)