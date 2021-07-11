from PyQt5.QtWidgets import QMainWindow

from controller import HomeController
from view.result.ui_result import Ui_Result


class ResultController(QMainWindow, Ui_Result):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.btnRepeat.clicked.connect(self.toAgain)
        self.btnClose.clicked.connect(self.endProgram)

    def toAgain(self):
        self.form = HomeController.HomeController()
        self.show()
        self.close()

    def endProgram(self):
        self.close()
        print('Program sukses')
