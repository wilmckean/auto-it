import PyQt5.QtWidgets as qtw
import sys

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto-IT")
        self.setLayout(qtw.QVBoxLayout())


        self.show()

app = qtw.QApplication([])
mw = MainWindow()
sys.exit(app.exec_())

