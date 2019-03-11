# Main dialog for creating email

import os

from PyQt5.QtWidgets import (QDialog,
                             QLineEdit,
                             QLabel,
                             QTextEdit,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QPushButton,
                             QFileDialog)


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

        self.sendPushButton = QPushButton('Se&nd')
        self.savePushButton = QPushButton('&Save')
        self.saveasPushButton = QPushButton('Save &As')

    def _properties(self):

        self.setWindowTitle('Create Email')
        self.resize(492, 347)

        self.fromLabel.setBuddy(self.fromLineEdit)
        self.toLabel.setBuddy(self.toLineEdit)
        self.subjectLabel.setBuddy(self.subjectLineEdit)
        self.messageLabel.setBuddy(self.messageTextEdit)

        self.sendPushButton.setEnabled(False)

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

        buttons_hbox = QHBoxLayout()
        buttons_hbox.addStretch(1)
        buttons_hbox.addWidget(self.sendPushButton)
        buttons_hbox.addWidget(self.savePushButton)
        buttons_hbox.addWidget(self.saveasPushButton)

        combined_vbox = QVBoxLayout()
        combined_vbox.addLayout(grid)
        combined_vbox.addLayout(buttons_hbox)

        self.setLayout(combined_vbox)

    def _connections(self):

        self.savePushButton.clicked.connect(self.on_savePushButton_clicked)
        self.saveasPushButton.clicked.connect(self.on_saveasPushButton_clicked)

    def on_savePushButton_clicked(self):

        sender = self.fromLineEdit.text()
        recipient = self.toLineEdit.text()
        subject = self.subjectLineEdit.text()
        message = self.messageTextEdit.toPlainText()

        print(f'sender: {sender}')
        print(f'recipient: {recipient}')
        print(f'subject: {subject}')
        print(f'message: {message}')

    def on_saveasPushButton_clicked(self):

        filename = QFileDialog.getSaveFileName(self, 'Save Email',
                                               os.getcwd(), 'Email (*.msg, *.eml)')

        print(f'filename: {filename}')

    def resizeEvent(self, event):

        print(f'{self.width()} x {self.height()}')
