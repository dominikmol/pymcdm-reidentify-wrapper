import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

import helpers
from index_ui import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # actions
        self.ui.import_data.clicked.connect(self.loadDataHandle)
        self.ui.bounds_gen_btn.clicked.connect(self.makeBoundsHandle)
        self.ui.calc_stfn.clicked.connect(lambda: helpers.calculateSTFN(self))


    def loadDataHandle(self):
        dialog = QFileDialog()
        dialog.setNameFilter("Data File (*.csv)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialogSuccesful = dialog.exec()

        if dialogSuccesful:
            selectedFile = dialog.selectedFiles()[0]
            self.ui.file_path.setText(selectedFile)
            print(selectedFile)
            helpers.loadData(self, selectedFile)
        else:
            print("File selection canceled")

    def makeBoundsHandle(self):
        self.bounds = helpers.make_bounds(self.data_matrix)
        formatted = ', '.join(f'({x}, {y})' for x, y in self.bounds)
        self.ui.bounds_data.setPlainText(formatted)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()