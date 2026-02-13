import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsScene, QMenu, QFileDialog
from PySide6.QtGui import QGuiApplication, QImage
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from io import BytesIO
import logic


np.set_printoptions(suppress=True, precision=4, linewidth=100)

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
        ax.set_title(f'$C^{{core}}={m:.4f}$')

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
        fig, ax = plt.subplots(dpi=300)#figsize=(12, 6), dpi=150, tight_layout=True)
        tfn_plot(fun, a, m, b, crit=i, ax=ax)
        canvas = FigureCanvas(fig)
        canvas.setContextMenuPolicy(Qt.CustomContextMenu)
        canvas.customContextMenuRequested.connect(
            lambda pos, c=canvas, f=fig: open_plot_menu(app, pos, c, f, "stfn_plot_core_"+str(index+1))
        )
        scene.addWidget(canvas)
        app.ui.gv_stfn_visualization.fitInView(
            scene.itemsBoundingRect(), Qt.KeepAspectRatio)
        plt.close(fig)
        app.stfn_plot_index = index


def show_mcda_rank_plot(app, expert_rank, rank, method):
    # Clear previous scene if exists
    scene = app.ui.gv_mcda_visualization.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.gv_mcda_visualization.setScene(scene)
    else:
        scene.clear()

    fig, ax = plt.subplots(dpi=300)#figsize=(12, 6), dpi=150, tight_layout=True)
    # Create bar plot with bars next to each other
    x = np.arange(len(rank))
    width = 0.4  # Width of the bars

    ax.bar(x - width / 2, expert_rank, width, color='blue', alpha=0.7, label='Expert Rank')
    ax.bar(x + width / 2, rank, width, color='orange', alpha=0.7, label='STFN Rank')

    # bars1 = ax.bar(x - width / 2, expert_rank, width, color='blue', alpha=0.7, label='Expert Rank')
    # bars2 = ax.bar(x + width / 2, rank, width, color='orange', alpha=0.7, label='STFN Rank')
    
    # ax.set_yticks(range(int(min(expert_rank)), int(max(expert_rank))+2))

    # Add scores above each bar
    # ax.bar_label(bars1, fmt='%.2f', padding=3, fontsize=8)
    # ax.bar_label(bars2, fmt='%.2f', padding=3, fontsize=8)

    # Add grid to the plot
    ax.grid(True, linestyle='--', alpha=0.7)

    ax.set_xlabel('Alternatives')
    ax.set_ylabel('Rank')
    # ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
    # ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.set_title(f'STFN-{method}')
    canvas = FigureCanvas(fig)
    canvas.setContextMenuPolicy(Qt.CustomContextMenu)
    canvas.customContextMenuRequested.connect(
        lambda pos, c=canvas, f=fig: open_plot_menu(app, pos, c, f, "mcda_rank_plot")
    )
    scene.addWidget(canvas)
    app.ui.gv_mcda_visualization.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)


def show_mcda_corelation_plot(app, expert_rank, rank, method):
    # Clear previous scene if exists
    scene = app.ui.gv_correlation_visualization.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.gv_correlation_visualization.setScene(scene)
    else:
        scene.clear()

    fig, ax = plt.subplots(dpi=300)#figsize=(12, 6), dpi=150, tight_layout=True)
    # Create bar plot with bars next to each other
    # x = np.arange(len(rank))
    ax.scatter(expert_rank, rank, color='black')
    ax.grid(True, linestyle=':')
    ax.set_xlabel("Expert rank")
    ax.set_ylabel(f"{method} rank")
    n = len(rank)
    ax.set_title(
        f"rw = {logic.rw(expert_rank, rank, n):.5f}\n WS = {logic.WS(expert_rank, rank, n):.5f}"
        )
    canvas = FigureCanvas(fig)
    canvas.setContextMenuPolicy(Qt.CustomContextMenu)
    canvas.customContextMenuRequested.connect(
        lambda pos, c=canvas, f=fig: open_plot_menu(app, pos, c, f, "correlation_plot")
    )
    scene.addWidget(canvas)
    app.ui.gv_correlation_visualization.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)


def open_plot_menu(app, pos, canvas, fig, default_name="plot"):
    menu = QMenu()
    menu.setStyleSheet("""
        QMenu {
            font-size: 11pt;
            padding: 6px;
        }
        QMenu::item {
            padding: 6px 20px;
        }
    """)

    copy_to_clipboard = menu.addAction("Copy to clipboard")
    save_png = menu.addAction("Save as PNG")
    save_pdf = menu.addAction("Save as PDF")
    save_svg = menu.addAction("Save as SVG")

    save_actions = [save_png, save_pdf, save_svg]

    action = menu.exec(canvas.mapToGlobal(pos))

    if not action:
        return
    
    if action == copy_to_clipboard:
        buf = BytesIO()
        fig.savefig(buf, format="png", dpi=300, bbox_inches="tight")
        buf.seek(0)

        image = QImage.fromData(buf.read(), "PNG")
        QGuiApplication.clipboard().setImage(image)
        return

    if action in save_actions:
        ext = action.text().split()[-1].lower()
        file_path, _ = QFileDialog.getSaveFileName(
            app,
            "Save plot",
            f"{default_name}.{ext}",
            f"{ext.upper()} (*.{ext})"
        )
        if file_path:
            fig.savefig(file_path, dpi=300, bbox_inches="tight")