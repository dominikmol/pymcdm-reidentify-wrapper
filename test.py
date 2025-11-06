import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

import helpers
from main_ui import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initial data
        self.stfn = None
        self.data = None
        self.data_matrix = None
        self.bounds = None
        self.weights = None
        self.types = None
        self.stfn_plot_data = []
        self.stfn_plot_index = 0

        # actions
        self.ui.btn_load_data.clicked.connect(self.load_data_handle)
        self.ui.btn_generate_bounds.clicked.connect(self.make_bounds_handle)
        self.ui.btn_calculate_stfn.clicked.connect(lambda: helpers.calculate_STFN(self))
        self.ui.btn_calculate_ranking.clicked.connect(lambda: helpers.calculate_MCDA(self))
        self.ui.txt_alternatives_ranking.textChanged.connect(self.change_expert_rank_handle)
        self.ui.btn_previous_visualization.clicked.connect(self.show_prev_stfn_plot)
        self.ui.btn_next_visualization.clicked.connect(self.show_next_stfn_plot)      

        # switching pages
        self.ui.btn_data_page.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.data_page))
        self.ui.btn_stfn_page.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.stfn_page))
        self.ui.btn_mcda_page.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.mcda_page))


    def load_data_handle(self):
        dialog = QFileDialog()
        dialog.setNameFilter("Data File (*.csv)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_successful = dialog.exec()

        if dialog_successful:
            selected_file = dialog.selectedFiles()[0]
            self.ui.txt_data_input.setText(selected_file)
            helpers.load_data(self, selected_file)
        else:
            print("File selection canceled")

    def make_bounds_handle(self):
        if self.data_matrix is None or self.data_matrix.size == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please import data first.')
            msg.setWindowTitle("Error")
            msg.exec()
            return
        self.bounds = helpers.make_bounds(self.data_matrix)
        formatted = ', '.join(f'({x}, {y})' for x, y in self.bounds)
        self.ui.txt_bounds_data.setPlainText(formatted)

    def change_expert_rank_handle(self):
        txt_alternatives_ranking = self.ui.txt_alternatives_ranking.toPlainText()
        self.ui.txt_old_ranking.setPlainText(txt_alternatives_ranking)

    def show_prev_stfn_plot(self):
        if self.stfn_plot_data:
            index = (self.stfn_plot_index - 1) % len(self.stfn_plot_data)
            helpers.show_stfn_plot(self, index)

    def show_next_stfn_plot(self):
        if self.stfn_plot_data:
            index = (self.stfn_plot_index + 1) % len(self.stfn_plot_data)
            helpers.show_stfn_plot(self, index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()