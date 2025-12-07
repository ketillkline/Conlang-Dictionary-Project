from PyQt6.QtWidgets import QApplication, QDialog
from GUI import MainWindow, DictionarySelectorDialog
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    selector = DictionarySelectorDialog()
    if selector.exec() == QDialog.DialogCode.Accepted:
        db_name = selector.get_selected_db()
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit()