import sys
from PyQt4 import QtGui,QtCore

class gui(QtGui.QMainWindow):
    def __init__(self):
        super(gui, self).__init__()
        self.iniciarJanela()

    def chegouInformacao(self):
        meu_cursor = self.output.textCursor()
        meu_cursor.movePosition(meu_cursor.End)
        meu_cursor.insertText(str(self.process.readAll()))
        self.output.ensureCursorVisible()

    def executarPrograma(self):
        # roda o processo
        # `start` recebe o programa executavel e a lista de argumentos
        self.process.start('ping',['127.0.0.1'])

    def iniciarJanela(self):
        # Layout eh melhor para colocar componentes
        meu_enquadramento = QtGui.QHBoxLayout()
        self.runButton = QtGui.QPushButton('Executar')
        self.runButton.clicked.connect(self.executarPrograma)

        self.output = QtGui.QTextEdit()

        meu_enquadramento.addWidget(self.output)
        meu_enquadramento.addWidget(self.runButton)

        componente_central = QtGui.QWidget()
        componente_central.setLayout(meu_enquadramento)
        self.setCentralWidget(componente_central)

        # Objeto QProcess para app externa
        self.process = QtCore.QProcess(self)
        
        # QProcess emite`readyRead` quando ha dados para ler
        self.process.readyRead.connect(self.chegouInformacao)

        # Prevenindo multiplas execucoes
        # desativando o botao quando o processo iniciar e reativando quando finalizar
        self.process.started.connect(lambda: self.runButton.setEnabled(False))
        self.process.finished.connect(lambda: self.runButton.setEnabled(True))


#Funcao principal inicio
def main():
    aplicacao = QtGui.QApplication(sys.argv)
    MinhaJanela = gui()
    MinhaJanela.show()
    sys.exit(aplicacao.exec_())
#fim da funcao principal

if __name__ == '__main__':
    main()
    
