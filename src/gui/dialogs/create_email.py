# Main dialog for creating email

from PyQt5.QtWidgets import (QDialog,
                             QLineEdit,
                             QLabel,
                             QTextEdit,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout)


class CreateEmailDialog(QDialog):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self._widgets()
        self._properties()
        self._layouts()
        self._connections()

    def _widgets(self):

        self.fromLabel = QLabel('&From:')
        self.toLabel = QLabel('&To:')
        self.subjectLabel = QLabel('Su&bject:')
        self.messageLabel = QLabel('M&essage:')

        self.fromLineEdit = QLineEdit()
        self.toLineEdit = QLineEdit()
        self.subjectLineEdit = QLineEdit()
        self.messageTextEdit = QTextEdit()

    def _properties(self):

        self.setWindowTitle('Create Email')
        self.resize(492, 347)

        self.fromLabel.setBuddy(self.fromLineEdit)
        self.toLabel.setBuddy(self.toLineEdit)
        self.subjectLabel.setBuddy(self.subjectLineEdit)
        self.messageLabel.setBuddy(self.messageTextEdit)

    def _layouts(self):

        grid = QGridLayout()
        grid.addWidget(self.fromLabel, 0, 0)
        grid.addWidget(self.fromLineEdit, 0, 1)
        grid.addWidget(self.toLabel, 1, 0)
        grid.addWidget(self.toLineEdit, 1, 1)
        grid.addWidget(self.subjectLabel, 2, 0)
        grid.addWidget(self.subjectLineEdit, 2, 1)
        grid.addWidget(self.messageLabel, 3, 0)
        grid.addWidget(self.messageTextEdit, 4, 0, 1, 2)

        self.setLayout(grid)

    def _connections(self):

        ...

    def resizeEvent(self, event):

        print(f'{self.width()} x {self.height()}')
