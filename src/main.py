# Inititiating spin! ~Cooper, Interstellar, 2014

import sys
from PyQt5.QtWidgets import QApplication
from src.gui.dialogs.create_email import CreateEmailDialog


APP = QApplication(sys.argv)


if __name__ == '__main__':

    dialog = CreateEmailDialog()
    dialog.show()
    APP.exec()

