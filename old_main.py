# import sys
from rich import print
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QFileDialog, QLabel
import old_helpers


class GUIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pymcdm-reidentify wrapper")
        self.resize(500, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.data_matrix = []

        # declaring widgets/inputs
        self.file_path = QLineEdit()
        self.browse_files = QPushButton("Import Data")
        self.types_label = QLabel("types of criteria")
        self.types = QLineEdit()
        self.calc_weights = QPushButton("Calculate TOPSIS weights with SITW")
        self.output = QTextEdit()

        # self.types.setText("1, 1, 1, -1, -1, -1, -1")
        self.types.setText("1, 1, 1, -1, -1")

        # actions
        self.browse_files.clicked.connect(self.clickHandle)
        # self.calc_weights.clicked.connect(self.calcSITW)
        self.calc_weights.clicked.connect(lambda: old_helpers.calculate_STFN(self))

        # adding widgets/inputs to layout
        layout.addWidget(self.file_path)
        layout.addWidget(self.browse_files)
        layout.addWidget(self.types_label)
        layout.addWidget(self.types)
        layout.addWidget(self.calc_weights)
        layout.addWidget(self.output)

    def clickHandle(self):
        dialog = QFileDialog()
        dialog.setNameFilter("Data File (*.csv)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialogSuccesful = dialog.exec()

        if dialogSuccesful:
            selectedFile = dialog.selectedFiles()[0]
            self.file_path.setText(selectedFile)
            print(selectedFile)
            # self.loadData(selectedFile)
            helpers.loadData(self, selectedFile)
        else:
            print("File selection canceled")


def main():
    app = QApplication([])
    app.setStyleSheet('''
        QWidget {
            font-size: 25px;
    }
        QPushButton {
            font-size: 25px;
        }              
    ''')
    window = GUIApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

# 1, 1, 1, -1, -1, -1, -1
