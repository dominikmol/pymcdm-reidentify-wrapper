from PySide6.QtWidgets import QMessageBox, QGraphicsScene


def showErrorMessage(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(title)
    msg.setInformativeText(message)
    msg.setWindowTitle("Error")
    msg.exec()

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