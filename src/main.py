import os
import sys
import ctypes

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

import data_manager
import logic
import visualization
from main_ui import Ui_MainWindow
import ui_helpers
import computation


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("RankTune-MCDA")

        # logo setup
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "assets", "rank-tune-logo.png")
        self.setWindowIcon(QIcon(icon_path))

        try:
            app_id = "ranktune.app"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        except Exception as e:
            print(f"Could not set AppUserModelID: {e}")

        # initial data
        self.stfn = None
        self.data = None
        self.data_matrix = None
        self.bounds = None
        self.weights = None
        self.types = None
        self.stfn_plot_data = []
        self.stfn_plot_index = 0
        self.expert_rank = None
        self.mcda_method = None
        self.new_rank = None
        self.stfn_mcda_body = None

        # actions
        self.ui.btn_load_data.clicked.connect(self.load_data_handle)
        self.ui.btn_generate_bounds.clicked.connect(self.make_bounds_handle)
        self.ui.btn_calculate_stfn.clicked.connect(lambda: computation.calculate_STFN(self))
        self.ui.btn_calculate_ranking.clicked.connect(
            lambda: computation.calculate_MCDA(self)
        )
        self.ui.btn_previous_visualization.clicked.connect(self.show_prev_stfn_plot)
        self.ui.btn_next_visualization.clicked.connect(self.show_next_stfn_plot)
        self.ui.btn_stfn_model_visualization.clicked.connect(
            lambda: visualization.show_rank_reversal_plot(self, "stfn")
        )
        self.ui.btn_expert_model_visualization.clicked.connect(
            lambda: visualization.show_rank_reversal_plot(self, "expert")
        )

        # switching pages
        self.ui.btn_data_page.clicked.connect(
            lambda: self.ui.pages.setCurrentWidget(self.ui.data_page)
        )
        self.ui.btn_stfn_page.clicked.connect(
            lambda: self.ui.pages.setCurrentWidget(self.ui.stfn_page)
        )
        self.ui.btn_mcda_page.clicked.connect(
            lambda: self.ui.pages.setCurrentWidget(self.ui.mcda_page)
        )
        self.ui.btn_reversal_page.clicked.connect(
            lambda: self.ui.pages.setCurrentWidget(self.ui.reversal_page)
        )

    def load_data_handle(self):
        dialog = QFileDialog()
        filters = "All Supported Files (*.csv *.txt *.xlsx *.xls);;CSV Files (*.csv);;Text Files (*.txt);;Excel Files (*.xlsx *.xls)"
        dialog.setNameFilter(filters)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if dialog.exec():
            selected_file = dialog.selectedFiles()[0]
            self.ui.txt_data_input.setText(selected_file)
            data_manager.load_data(self, selected_file)

    def make_bounds_handle(self):
        if self.data_matrix is None or self.data_matrix.size == 0:
            ui_helpers.showErrorMessage("Error", "Please import data first.")
            return
        self.bounds = logic.make_bounds(self.data_matrix)
        formatted = ", ".join(f"({x}, {y})" for x, y in self.bounds)
        self.ui.txt_bounds_data.setPlainText(formatted)

    def show_prev_stfn_plot(self):
        if self.stfn_plot_data:
            index = (self.stfn_plot_index - 1) % len(self.stfn_plot_data)
            visualization.show_stfn_plot(self, index)

    def show_next_stfn_plot(self):
        if self.stfn_plot_data:
            index = (self.stfn_plot_index + 1) % len(self.stfn_plot_data)
            visualization.show_stfn_plot(self, index)

    def success_handler(self, stfn, extra_data):
        self.stfn = stfn
        computation.on_stfn_calculated(self, stfn, **extra_data)

    def error_handler(self, msg):
        computation.on_stfn_error(self, msg)

    def progress_handler(self, epoch, max_epochs):
        procentage = int((epoch / max_epochs) * 100)
        self.ui.progressBar.setValue(procentage)

    def _refit_all_graphics_views(self):
        for gv in [
            self.ui.gv_stfn_visualization,
            self.ui.gv_mcda_visualization,
            self.ui.gv_correlation_visualization,
            self.ui.gv_rank_reversal,
        ]:
            if gv.scene() and gv.scene().itemsBoundingRect().isValid():
                gv.fitInView(gv.scene().itemsBoundingRect(), Qt.KeepAspectRatio)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._refit_all_graphics_views()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
