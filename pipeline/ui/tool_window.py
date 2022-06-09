import os.path

from PySide2.QtWidgets import QApplication, QDialog, QLineEdit
from Qt import QtCompat, QtCore, QtWidgets
import six
import sys

from pipeline.utils import resolver


if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

try :
    import pymel.core as pm
    in_maya = True
except:
    pm = None
    in_maya = False

ui_path = Path(__file__).parent /"qt"/ "browser_window.ui"
UserRole = QtCore.Qt.UserRole


class ToolWindow(QDialog):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)

        self.open.clicked.connect(self.do_open)

        self.fill_cats()


    def fill_cats(self):
        for file in resolver.get_cats("MOVIE"):
            fill_items(self.listCat, file, os.path.basename(file))


    def do_open(self):
        result = None
        pm.openFile(result)


def fill_items(listWidget, label, data):
    item = QtWidgets.QListWidgetItem()
    item.setText(label)
    item.setData(UserRole, data)  # facultatif, permet de récupérer les datas, mais pas obligatoire
    listWidget.addItem(item)
    return item


#### Test ####

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = ToolWindow()
    t.show()
    app.exec_()