import sys
from PyQt4 import QtGui,QtCore

class gui(QtGui.QMainWindow):
    def __init__(self):
        super(gui, self).__init__()
        self.initUI()

    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll()))
        self.output.ensureCursorVisible()

    def callProgram(self):
        # run the process
        # `start` takes the exec and a list of arguments
        self.process.start('ping',['127.0.0.1'])

    def initUI(self):
        # Layout eh melhor para colocar componentes
        layout = QtGui.QHBoxLayout()
        self.runButton = QtGui.QPushButton('Run')
        self.runButton.clicked.connect(self.callProgram)

        self.output = QtGui.QTextEdit()

        layout.addWidget(self.output)
        layout.addWidget(self.runButton)

        centralWidget = QtGui.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # Objeto QProcess para app externa
        self.process = QtCore.QProcess(self)
        
        # QProcess emite`readyRead` quando ha dados para ler
        self.process.readyRead.connect(self.dataReady)

        # Prevenindo multiplas execucoes
        # desativando o botao quando o processo iniciar e reativando quando finalizar
        self.process.started.connect(lambda: self.runButton.setEnabled(False))
        self.process.finished.connect(lambda: self.runButton.setEnabled(True))


#Funcao principal inicio
def main():
    app = QtGui.QApplication(sys.argv)
    ui=gui()
    ui.show()
    sys.exit(app.exec_())
#fim da funcao principal

if __name__ == '__main__':
    main() 
