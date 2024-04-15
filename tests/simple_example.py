from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout
from PyQt5.QtWidgets import QGraphicsBlurEffect
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Open Dialog", self)
        self.button.clicked.connect(self.open_dialog)

        self.setCentralWidget(self.button)

    def open_dialog(self):
        self.blur_effect = QGraphicsBlurEffect()
        self.setGraphicsEffect(self.blur_effect)

        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Dialog")
        self.dialog.finished.connect(self.remove_blur)

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Close", clicked=self.dialog.close))

        self.dialog.setLayout(layout)
        self.dialog.exec_()

    def remove_blur(self):
        self.setGraphicsEffect(None)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()