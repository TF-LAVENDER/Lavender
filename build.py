
import os
import site
from PyInstaller.__main__ import run

pyside6_dir = site.getsitepackages()[0] + "\\PySide6"

opts = [
    'LavenderMain.py',
    '--onefile',
    '--noconsole',
    '--name', 'test2',
    '--add-data', 'MainWindow.ui:.',
    '--add-data', 'images:images',
    '--add-data', 'components:components'
]

run(opts)
