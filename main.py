import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

import helpers
from index_ui import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initial data
        self.stfn = None
        self.data_matrix = None
        self.stfn_plot_data = []
        self.stfn_plot_index = 0  

        # actions
        self.ui.import_data.clicked.connect(self.load_data_handle)
        self.ui.bounds_gen_btn.clicked.connect(self.make_bounds_handle)
        self.ui.calc_stfn.clicked.connect(lambda: helpers.calculate_STFN(self))
        self.ui.calc_mcda.clicked.connect(lambda: helpers.calculate_MCDA(self))
        self.ui.expert_rank.textChanged.connect(self.change_expert_rank_handle)
        self.ui.prev_plot_btn_stfn.clicked.connect(self.show_prev_stfn_plot)
        self.ui.next_plot_btn_stfn.clicked.connect(self.show_next_stfn_plot)              


    def load_data_handle(self):
        dialog = QFileDialog()
        dialog.setNameFilter("Data File (*.csv)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_successful = dialog.exec()

        if dialog_successful:
            selected_file = dialog.selectedFiles()[0]
            self.ui.file_path.setText(selected_file)
            print(selected_file)
            helpers.load_data(self, selected_file)
        else:
            print("File selection canceled")

    def make_bounds_handle(self):
        self.bounds = helpers.make_bounds(self.data_matrix)
        formatted = ', '.join(f'({x}, {y})' for x, y in self.bounds)
        self.ui.bounds_data.setPlainText(formatted)

    def change_expert_rank_handle(self):
        expert_rank = self.ui.expert_rank.text()
        self.ui.ranking_old.setPlainText(expert_rank)

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