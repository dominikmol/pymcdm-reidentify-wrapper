from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from pymcdm.correlations import weighted_spearman
from pymcdm.helpers import leave_one_out_rr
from pymcdm.visuals import rankings_flow_correlation
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, QImage
from PySide6.QtWidgets import QFileDialog, QGraphicsScene, QMenu

import logic

np.set_printoptions(suppress=True, precision=4, linewidth=100)


def tfn_plot(tfn, a, m, b, crit=None, plot_kwargs=dict(), text_kwargs=dict(), ax=None):

    if ax is None:
        ax = plt.gca()

    plot_kwargs = dict(linestyle="-", color="black") | plot_kwargs

    text_kwargs = dict(color="black") | text_kwargs

    width = abs(b - a)
    start = a - width * 0.1
    stop = b + width * 0.1
    x = np.linspace(start, stop, 150)

    ax.plot(x, tfn(x), **plot_kwargs)

    if crit is not None:
        ax.annotate(
            f"$C_{crit}^{{core}}$", (m - abs(b - a) * 0.01, 1.05), **text_kwargs
        )
        ax.set_title(f"$C_{crit}^{{core}}={m:.2f}$")
    else:
        ax.annotate(f"$C^{{core}}$", (m - abs(b - a) * 0.01, 1.05), **text_kwargs)
        ax.set_title(f"$C^{{core}}={m:.4f}$")

    ax.grid(True, linestyle="--", alpha=0.2, color="black")
    ax.set_axisbelow(True)
    ax.set_ylim(0, 1.3)

    ax.set_ylabel(r"$\mu(x)$")
    ax.set_xlabel("x")

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
        fig, ax = plt.subplots(dpi=300)
        tfn_plot(fun, a, m, b, crit=i, ax=ax)
        canvas = FigureCanvas(fig)
        canvas.setContextMenuPolicy(Qt.CustomContextMenu)
        canvas.customContextMenuRequested.connect(
            lambda pos, c=canvas, f=fig: open_plot_menu(
                app, pos, c, f, f"stfn_plot_core_{index + 1}_plot"
            )
        )
        scene.addWidget(canvas)
        app.ui.gv_stfn_visualization.fitInView(
            scene.itemsBoundingRect(), Qt.KeepAspectRatio
        )
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

    fig, ax = plt.subplots(dpi=300)
    # Create bar plot with bars next to each other
    x = np.arange(len(rank))
    width = 0.4  # Width of the bars

    ax.bar(
        x - width / 2, expert_rank, width, color="blue", alpha=0.7, label="Expert Rank"
    )
    ax.bar(x + width / 2, rank, width, color="orange", alpha=0.7, label="STFN Rank")

    # Add grid to the plot
    ax.grid(True, linestyle="--", alpha=0.7)

    ax.set_xlabel("Alternatives")
    ax.set_ylabel("Rank")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=2)
    ax.set_title(f"STFN-{method}")
    canvas = FigureCanvas(fig)
    canvas.setContextMenuPolicy(Qt.CustomContextMenu)
    canvas.customContextMenuRequested.connect(
        lambda pos, c=canvas, f=fig: open_plot_menu(
            app, pos, c, f, f"mcda_{method}_rank_plot"
        )
    )
    scene.addWidget(canvas)
    app.ui.gv_mcda_visualization.fitInView(
        scene.itemsBoundingRect(), Qt.KeepAspectRatio
    )


def show_mcda_corelation_plot(app, expert_rank, rank, method):
    # Clear previous scene if exists
    scene = app.ui.gv_correlation_visualization.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.gv_correlation_visualization.setScene(scene)
    else:
        scene.clear()

    fig, ax = plt.subplots(dpi=300)
    ax.scatter(expert_rank, rank, color="black")
    ax.grid(True, linestyle=":")
    ax.set_xlabel("Expert rank")
    ax.set_ylabel(f"{method} rank")
    n = len(rank)
    ax.set_title(
        f"rw = {logic.rw(expert_rank, rank, n):.5f}\n WS = {logic.WS(expert_rank, rank, n):.5f}"
    )
    canvas = FigureCanvas(fig)
    canvas.setContextMenuPolicy(Qt.CustomContextMenu)
    canvas.customContextMenuRequested.connect(
        lambda pos, c=canvas, f=fig: open_plot_menu(
            app, pos, c, f, f"{method}_correlation_plot"
        )
    )
    scene.addWidget(canvas)
    app.ui.gv_correlation_visualization.fitInView(
        scene.itemsBoundingRect(), Qt.KeepAspectRatio
    )


def show_rank_reversal_plot(app, reversal_type):
    # Clear previous scene if exists
    scene = app.ui.gv_rank_reversal.scene()
    if scene is None:
        scene = QGraphicsScene()
        app.ui.gv_rank_reversal.setScene(scene)
    else:
        scene.clear()

    types = np.ones(len(app.bounds))
    if reversal_type == "expert":
        types = logic.get_types_from_cores(app.stfn.cores, app.bounds)

    body = None
    if reversal_type == "expert":
        body = logic.generate_mcda_body(app.mcda_method)
    if reversal_type == "stfn":
        body = app.stfn_mcda_body

    rankings, corr, labels = leave_one_out_rr(
        method=body,
        matrix=app.data_matrix,
        weights=app.weights,
        types=types,
        corr_function=weighted_spearman,
        only_rr=False,
    )

    # plot scaling with number of rankings
    num_rankings = len(rankings)
    figsize_height = max(8, num_rankings * 0.25)
    figsize_width = max(10, num_rankings * 0.6)

    fig, ax = plt.subplots(figsize=(figsize_width, figsize_height), dpi=300)
    ax, cax = rankings_flow_correlation(
        rankings=rankings,
        correlations=corr,
        labels=labels,
        correlation_plot_kwargs=dict(space_multiplier=0.15),
        ranking_flows_kwargs=dict(better_grid=True),
        correlation_ax_size="10%",
        ax=ax,
    )
    cax.set_ylim(0.75, 1.05)
    title = (
        f"{reversal_type.upper()}-Based {app.mcda_method.upper()} Rank Reversal Model"
    )
    plt.title(title)
    plt.tight_layout(pad=1.0)
    canvas = FigureCanvas(fig)
    canvas.setContextMenuPolicy(Qt.CustomContextMenu)
    canvas.customContextMenuRequested.connect(
        lambda pos, c=canvas, f=fig: open_plot_menu(
            app, pos, c, f, f"{reversal_type}_{app.mcda_method}_rank_reversal_plot"
        )
    )
    scene.addWidget(canvas)
    app.ui.gv_rank_reversal.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)


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

    save_actions = [save_png, save_pdf]

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
            app, "Save plot", f"{default_name}.{ext}", f"{ext.upper()} (*.{ext})"
        )
        if file_path:
            fig.savefig(file_path, dpi=300, bbox_inches="tight")
