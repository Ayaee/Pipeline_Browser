from PySide2.QtWidgets import QApplication, QDialog, QLineEdit
from Qt import QtCompat, QtCore
import six
import sys

from pipeline.utils import dialogs

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


class ToolWindow(QDialog):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)

        """self.build.clicked.connect(self.do_choose)
        if in_maya :
            self.buildOpen.clicked.connect(self.do_open)
        else :
            self.buildOpen.setEnabled(False)
            #pass
            #bouton grisée
        self.choose.addItems(["Modeling", "Surfacing", "Rigging"])"""


    """def do_choose(self):
        self.entry = self.findChild(QLineEdit, "entry")
        nameAsset = self.entry.text()
        print(nameAsset)
        choose = str(self.choose.currentText())
        result = None
        if choose == "Modeling":
            from pipeline.maya.tools.build import modeling_build as modeling
            result = modeling.build(nameAsset)
        elif choose == "Surfacing":
            try:
                from pipeline.maya.tools.build import surfacing_build as surfacing
                result = surfacing.build(nameAsset)
            except Exception as ex:
                dialogs.Dialogs().warn(ex)
        else:
            try:
                from pipeline.maya.tools.build import rigging_build as rigging
                result = rigging.build(nameAsset)
            except Exception as ex:
                dialogs.Dialogs().warn(ex)
        return result"""

    """def do_open(self):
        result = self.do_choose()
        pm.openFile(result)"""


def open():
    app = QApplication(sys.argv)
    t = ToolWindow()
    t.show()
    app.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = ToolWindow()
    t.show()
    app.exec_()