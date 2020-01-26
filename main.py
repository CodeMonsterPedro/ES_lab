from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QDialog, QLineEdit, QRadioButton
from mainwindow import Ui_MainWindow
import sys
import pickle
from fpdf import FPDF, HTMLMixin
from dialogs import AnswerAddDialog, NodeAddDialog, NodeDialog


class MyFPDF(FPDF, HTMLMixin):
    pass


class Node:
    dialog = 0

    def __init__(self, text='empty node', id=0):
        self.id = id
        self._text = text
        self._childs = []
        self._childs.append(Answer())
        self._childs.append(Answer())

    def run(self):
        Node.dialog.setText(self._text)
        Node.dialog.exec_()
        return Node.dialog.getAnswer()

    def who(self):
        return 'Node'

    def setText(self, text):
        self._text = text

    def getText(self):
        return self._text

    def setChilds(self, item1, item2):
        self._childs[0] = item1
        self._childs[1] = item2

    def setFirstChild(self, item):
        self._childs[0] = item

    def setSecoundChild(self, item):
        self._childs[1] = item

    def getFirstChild(self):
        return self._childs[0]

    def getSecoundChild(self):
        return self._childs[1]


class Answer:
    answers = []
    msg = 0

    def __init__(self, text='empty question', id=0):
        self.id = id
        self._text = text

    def run(self):
        if Answer.msg != 0:
            Answer.msg.setText(self._text)
            Answer.msg.exec_()
            return 'Finish'

    def who(self):
        return 'Answer'

    def setText(self, text):
        self._text = text

    def getText(self):
        return self._text


class SystemControl(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self._topLablesTest = ('Question', 'Answer')
        self._topLabelsStructure = ('Node id', 'Childs')
        self._testList = [] # keeps questions and answers on it, for displaing it in the future
        self._structureList = [] # keeps nods and its childs, for displaing it in the future
        self._entryNode = 0 # start node
        self._idLevel = 0
        self._finalAnswer = ''
        self._answerValuesList = []
        Answer.msg = QMessageBox()
        Answer.answers = self._answerValuesList
        Node.dialog = NodeDialog()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tbw_test.setColumnCount(2)
        self.ui.tbw_structure.setColumnCount(2)
        self.ui.tbw_test.setHorizontalHeaderLabels(self._topLablesTest)
        self.ui.tbw_structure.setHorizontalHeaderLabels(self._topLabelsStructure)
        self.ui.btn_run.clicked.connect(self.run)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_upload.clicked.connect(self.upload)
        self.ui.btn_makefile.clicked.connect(self.makeFile)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_nodereset.clicked.connect(self.addNode)
        self.ui.btn_answerreset.clicked.connect(self.addAnswer)
        # set node
        # set answer

# items add

    def addNode(self):
        id = int(self.ui.ln_nodereset.text())
        self.setNode(id)

    def addAnswer(self):
        id = int(self.ui.ln_answerreset.text())
        self.setAnswer(id)

    def setNode(self, id):
        n = self.getNode(id)
        dialog = NodeAddDialog()
        item = 0
        if n and n == self._entryNode:
            item = n
        else:
            if n and n[0] == 1:
                item = n[1].getFirstChild()
            if n and n[0] == 2:
                item = n[1].getSecoundChild()
            if n and item.who() == 'Answer':
                x = Node()
                if n[0] == 1:
                    n[1].setFirstChild(x)
                    item = n[1].getFirstChild()
                else:
                    n[1].setSecoundChild(x)
                    item = n[1].getSecoundChild()
        if dialog.setNode(item):
            dialog.exec_()
            self.idSetup()
            self.structureListUpdate()

    def setAnswer(self, id):
        n = self.getNode(id)
        dialog = AnswerAddDialog()
        item = 0
        if n and n == self._entryNode:
            item = n
        else:
            if n and n[0] == 1:
                item = n[1].getFirstChild()
            if n and n[0] == 2:
                item = n[1].getSecoundChild()
            if n and n[1].who() == 'Node':
                x = Answer()
                if n[0] == 1:
                    n[1].setFirstChild(x)
                    item = n[1].getFirstChild()
                else:
                    n[1].setSecoundChild(x)
                    item = n[1].getSecoundChild()
        if dialog.setNode(item): 
            dialog.exec_()
            self.idSetup()
            self.structureListUpdate()

    def getNode(self, id):
        if self._entryNode == 0:
            self._entryNode = Node()
            return self._entryNode
        elif self._entryNode.id == id:
            return self._entryNode
        else:
            f = self._entryNode.getFirstChild()
            if f.id == id:
                return (1, self._entryNode)
            elif f.who() == 'Node':
                res = self.nextNode(self._entryNode.getFirstChild(), id)
                if res:
                    return res
            s = self._entryNode.getSecoundChild()
            if s.id == id:
                return (2, self._entryNode)
            elif s.who() == 'Node':
                res = self.nextNode(self._entryNode.getSecoundChild(), id)
                if res:
                    return res
            return False

    def nextNode(self, node, id):
        print(node.id)
        f = node.getFirstChild()
        if f.id == id:
            return (1, node)
        elif f.who() == 'Node':
            res = self.nextNode(node.getFirstChild(), id)
            if res:
                return res
        s = node.getSecoundChild()
        if s.id == id:
            return (2, node)
        elif s.who() == 'Node':
            res = self.nextNode(node.getSecoundChild(), id)
            if res:
                return res
        return False
# /items add
# tables add
    def addItemToTestList(self, item):
        tSize = self.ui.tbw_test.rowCount()
        self.ui.tbw_test.insertRow(tSize)
        self.ui.tbw_test.setItem(tSize, 0, QTableWidgetItem(item[0]))
        self.ui.tbw_test.setItem(tSize, 1, QTableWidgetItem(item[1]))
        self._testList.append(item)

    def testListClear(self):
        for i in range(self.ui.tbw_test.rowCount(), -1, -1):
            self.ui.tbw_test.removeRow(i)

    def structureListUpdate(self):
        nodes = self.getNodesList()
        self.structureListClear()
        for i in range(len(nodes)):
            self.ui.tbw_structure.insertRow(i)
            self.ui.tbw_structure.setItem(i, 0, QTableWidgetItem(nodes[i][0]))
            self.ui.tbw_structure.setItem(i, 1, QTableWidgetItem(nodes[i][1]))

    def getNodesList(self):
        nodesList = list()
        self.getNodeData(self._entryNode, nodesList)
        return nodesList
    
    def getNodeData(self, node, nodesList):
        me = '{} {}'.format(node.id, node.who())
        contains = ''
        if node.who() == 'Answer':
            contains = 'End'
            nodesList.append((me, contains))
        else:
            firstChild = node.getFirstChild()
            firstChildText = '{} {}'.format(firstChild.id, firstChild.who())
            secoundChild = node.getSecoundChild()
            secoundChildText = '{} {}'.format(secoundChild.id, secoundChild.who())
            contains = '{}, {}'.format(firstChildText, secoundChildText)
            nodesList.append((me, contains))
            self.getNodeData(firstChild, nodesList)
            self.getNodeData(secoundChild, nodesList)

    def structureListClear(self):
        for i in range(self.ui.tbw_structure.rowCount(), -1, -1):
            self.ui.tbw_structure.removeRow(i)


# /tables add
# set ids

    def idSetup(self):
        topId = list()
        topId.append(1)
        if self._entryNode != 0:
            self._entryNode.id = topId[0]
            topId[0] += 1
            self.setId(self._entryNode.getFirstChild(), topId)
            self.setId(self._entryNode.getSecoundChild(), topId)

    def setId(self, node, topId):
        node.id = topId[0]
        topId[0] += 1
        if node.who() == 'Node':
            self.setId(node.getFirstChild(), topId)
            self.setId(node.getSecoundChild(), topId)
# /set ids

# run

    def run(self):
        self.testListClear()
        if self._entryNode != 0:
            self.runNext(self._entryNode)

    def runNext(self, item):
        if item.who() == 'Node':
            res = item.run()
            me = '{} {} {}'.format(item.id, item.who(), item.getText())
            contains = '{}'.format(str(res))
            self.addItemToTestList((me, contains))
            nextItem = 0
            if res:
                self._answerValuesList.append(item.id)
                nextItem = item.getFirstChild()
                self.runNext(nextItem)
            else:
                self._answerValuesList.append(-item.id)
                nextItem = item.getSecoundChild()
                self.runNext(nextItem)
        elif item.who() == 'Answer':
            item.run()
            me = '{} {} {}'.format(item.id, item.who(), item.getText())
            contains = 'End'
            self.addItemToTestList((me, contains))
# /run

# additional 

    def clear(self):
        self._mainTree = []
        self._entryNode = 0
        self._answerValuesList = []
        self.testListClear()
        self.structureListClear()

    def makeFile(self):
        pdf = MyFPDF()
        pdf.add_page()
        html = '<h1>ES output file</h1><table border="1" width="50%"><thead><tr><th width="50%">Question</th><th  width="50%">Answer</th></tr></thead><tbody>'
        for row in self._testList:
            html += '<tr><td>{}</td><td>{}</td></tr>'.format(row[0], row[1])
        html += '</tbody></table>'
        pdf.write_html(html)
        pdf.output('output.pdf')

    def upload(self):
        f = open('base', 'rb')
        self = pickle.load(f)
        f.close()

    def save(self):
        f = open('base', 'wb')
        pickle.dump(self, f)
        f.close()
# /additional


if __name__ == "__main__":
    app = QApplication([])
    window = SystemControl()
    window.show()
    sys.exit(app.exec_())
