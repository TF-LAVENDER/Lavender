from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QWidget
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

def load_ui_file(path) -> QWidget:
    loader = QUiLoader()
    file = QFile(path)
    file.open(QFile.ReadOnly)
    ui = loader.load(file)
    file.close()
    return ui
