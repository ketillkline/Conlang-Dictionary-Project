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

        tabs = QTabWidget()
        tabs.addTab(DictionaryTab(), "Dictionary")
        tabs.addTab(PhonologyTab(), "Phonology")


class TemplateTab(QWidget):
    def __init__(self):
        super().__init__()


class DictionarySelectorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Picking")
        self.resize(500, 500)

        add_new = QPushButton("Add new language")
        add_new.clicked.connect(self.add_new)
        combo_box = QComboBox()
        combo_box_label = QLabel("Pick a language")

        layout = QGridLayout()
        layout.addWidget(add_new)
        if combo_box:
            layout.addWidget(combo_box)
        self.setLayout(layout)

    def add_new(self):
        window = CreateNewLanguage()
        window.exec()

    def get_selected_db(self):
        pass

class PhonologyTab(TemplateTab):
    def __init__(self):
        super().__init__()

class DictionaryTab(TemplateTab):
    def __init__(self):
        super().__init__()

class PopUpTemplate(QDialog):
    def __init__(self):
        super().__init__()

    def add_new_lang(self, db_name: str):
        db_name = DatabaseManager(db_name)


class CreateNewLanguage(PopUpTemplate):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New Language")
        self.resize(300, 300)

        welcome_label = QLabel("Welcome to my Conlang App!\nLet's get started with some basic info.")
        name_label = QLabel("Name")
        name_input = QLineEdit()

        enter_button = QPushButton("Done")


        widgets = [welcome_label, name_label]

        layout = QGridLayout()


