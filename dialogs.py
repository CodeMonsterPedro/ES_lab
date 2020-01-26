from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QDialog, QLineEdit, QRadioButton
import sys
import pickle


class AnswerAddDialog(QDialog):
    def __init__(self, parent=None, text=''):
        super(AnswerAddDialog, self).__init__(parent)
        self._node = 0
        self._text = text
        self._ln_answer = QLineEdit()
        self._btn_yes = QPushButton("Ok")
        self._btn_yes.clicked.connect(self.accept)
        layoutV = QVBoxLayout()
        layoutV.addWidget(self._ln_answer)
        layoutV.addWidget(self._btn_yes)
        self.setLayout(layoutV)

    def accept(self):
        self._node.setText(self._ln_answer.text())
        self.close()

    def setNode(self, node):
        if node:
            self._node = node
            self._ln_answer.setText(self._node.getText())
            return True
        else:
            return False


class NodeAddDialog(QDialog):
    def __init__(self, parent=None, text='',):
        super(NodeAddDialog, self).__init__(parent)
        self._node = 0
        self._text = text
        self._answer = []
        self._answer.append(0)
        self._answer.append(0)
        self.ln_question = QLineEdit()
        self.ln_question.setText(self._text)
        self.ln_question.editingFinished.connect(self.setText)
        self.layoutH1 = QHBoxLayout()
        self.btn_add = QPushButton()
        self.btn_add.setText('Add')
        self.btn_cansel = QPushButton()
        self.btn_cansel.setText('Cansel')
        self.btn_add.clicked.connect(self.addNode)
        self.btn_cansel.clicked.connect(self.decline)
        self.layoutH1.addWidget(self.btn_add)
        self.layoutH1.addWidget(self.btn_cansel)
        self.layoutH2 = QHBoxLayout()
        self.rb_node1 = QRadioButton()
        self.rb_node1.setText('Node1')
        self.rb_answer1 = QRadioButton()
        self.rb_answer1.setText('Answer1')
        self.rb_answer1.setChecked(True)
        self.layoutH2.addWidget(self.rb_node1)
        self.layoutH2.addWidget(self.rb_answer1)
        self.layoutH3 = QHBoxLayout()
        self.rb_node2 = QRadioButton()
        self.rb_node2.setText('Node2')
        self.rb_answer2 = QRadioButton()
        self.rb_answer2.setText('Answer2')
        self.rb_answer2.setChecked(True)
        self.layoutH3.addWidget(self.rb_node2)
        self.layoutH3.addWidget(self.rb_answer2)
        self.layoutV = QVBoxLayout()
        self.layoutV.addWidget(self.ln_question)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH1)
        self.setLayout(self.layoutV)

    def addNode(self):
        self._node.setText(self.ln_question.text())
        if self.rb_node1.isChecked() and self._node.getFirstChild().who() == 'Answer':
            self._node.setFirstChild(Node())
        if self.rb_answer1.isChecked() and self._node.getFirstChild().who() == 'Node':
            self._node.setFirstChild(Answer())
        if self.rb_node2.isChecked() and self._node.getSecoundChild().who() == 'Answer':
            self._node.setSecoundChild(Node())
        if self.rb_answer2.isChecked() and self._node.getSecoundChild().who() == 'Node':
            self._node.setSecoundChild(Answer())
        self.close()

    def decline(self):
        self.close()

    def setText(self):
        self._node.setText(self.ln_question.text())

    def setNode(self, node):
        if node:
            self._node = node
            if self._node.getFirstChild().who() == 'Answer':
                self.rb_answer1.setChecked(True)
                self.rb_node1.setChecked(False)
            else: 
                self.rb_answer1.setChecked(False)
                self.rb_node1.setChecked(True)
            if self._node.getSecoundChild().who() == 'Answer':
                self.rb_answer2.setChecked(True)
                self.rb_node2.setChecked(False)
            else: 
                self.rb_answer2.setChecked(False)
                self.rb_node2.setChecked(True)
            return True
        else:
            return False


class NodeDialog(QDialog):
    def __init__(self, parent=None, text=''):
        super(NodeDialog, self).__init__(parent)
        self._answer = 0
        self._label = QLabel(text)
        self._btn_yes = QPushButton("Yes")
        self._btn_no = QPushButton('No')
        self._btn_yes.clicked.connect(self.accept)
        self._btn_no.clicked.connect(self.decline)
        layoutH = QHBoxLayout()
        layoutH.addWidget(self._btn_yes)
        layoutH.addWidget(self._btn_no)
        layoutV = QVBoxLayout()
        layoutV.addWidget(self._label)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def setText(self, text):
        self._label.setText(text)

    def accept(self):
        self._answer = True
        self.close()

    def decline(self):
        self._answer = False
        self.close()

    def getAnswer(self):
        return self._answer
