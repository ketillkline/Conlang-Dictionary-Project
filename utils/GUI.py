from PyQt6.QtWidgets import(QWidget, QLabel, QPushButton, QVBoxLayout,
                             QGridLayout, QLineEdit, QApplication,
                             QMainWindow, QToolBar, QTextEdit, QDialog, QTabWidget, QScrollArea, QComboBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QFont, QIcon
from database import DatabaseManager
import sys, winsound

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()



class DictionarySelectorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Picking")
        self.resize(500, 500)
        combo_box = QComboBox()

        layout = QGridLayout()
        layout.addWidget(combo_box)
        self.setLayout(layout)

    def get_selected_db(self):
        pass
