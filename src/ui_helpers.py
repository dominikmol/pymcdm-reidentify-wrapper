from io import BytesIO

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QGraphicsScene, QTableWidgetItem, QFileDialog, QMenu
from PySide6.QtGui import QGuiApplication, QImage


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
            item.setTextAlignment(
                Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
            )
            table.setItem(row, col, item)

    header = table.horizontalHeader()
    header.setSectionResizeMode(header.ResizeMode.Stretch)
    header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap)

    table.executeDelayedItemsLayout()

    padding = 10
    max_height = 20
    for i in range(table.columnCount()):
        current_width = header.sectionSize(i)
        text = table.horizontalHeaderItem(i).text()
        rect = header.fontMetrics().boundingRect(
            0,
            0,
            current_width - 10,
            1000,
            Qt.TextFlag.TextWordWrap | Qt.AlignmentFlag.AlignCenter,
            text,
        )
        col_height = rect.height()
        if col_height > max_height:
            max_height = col_height

    header.setFixedHeight(max_height + padding)
    table.setWordWrap(True)
    table.setAlternatingRowColors(True)
    table.resizeRowsToContents()


def disable_all_buttons(app):
    app.ui.btn_load_data.setEnabled(False)
    app.ui.btn_generate_bounds.setEnabled(False)
    app.ui.btn_calculate_stfn.setEnabled(False)
    app.ui.btn_calculate_ranking.setEnabled(False)
    app.ui.btn_previous_visualization.setEnabled(False)
    app.ui.btn_next_visualization.setEnabled(False)
    app.ui.btn_expert_model_visualization.setEnabled(False)
    app.ui.btn_stfn_model_visualization.setEnabled(False)


def enable_all_buttons(app):
    app.ui.btn_load_data.setEnabled(True)
    app.ui.btn_generate_bounds.setEnabled(True)
    app.ui.btn_calculate_stfn.setEnabled(True)
    app.ui.btn_calculate_ranking.setEnabled(True)
    app.ui.btn_previous_visualization.setEnabled(True)
    app.ui.btn_next_visualization.setEnabled(True)
    app.ui.btn_expert_model_visualization.setEnabled(True)
    app.ui.btn_stfn_model_visualization.setEnabled(True)

def clear_or_set_scene(graphics_view):
    scene = graphics_view.scene()
    if scene is None:
        scene = QGraphicsScene()
        graphics_view.setScene(scene)
    else:
        scene.clear()
    return scene


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