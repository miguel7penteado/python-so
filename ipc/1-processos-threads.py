
from threading import Thread
from Queue import Queue
import datetime
import subprocess

# numero_de_threads
numero_threads = 100
fila_de_threads = Queue()
resultado_saida = []

def meu_verificador(identificador_numerico, parametro_fila):
    while True:
        endereco_consultado = parametro_fila.get().replace("\n", "")
        data_hora_atual = datetime.datetime.now()
        
        # Ping para checar se esta on-line
        
        processo = subprocess.Popen("ping -c 1 %s" % endereco_consultado, shell=FALSE, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
        processo.wait()
        print("O identificador desse processo eh %d" % processo.pid) 
        print("\neste processo foi chamado na thread %d" % identificador_numerico)
        
        if processo.returncode == 0:
            resultado_saida.append("{0} {1} Deu certo ".format(endereco_consultado, data_hora_atual.strftime("horario %Y/%m/%d-%H:%M:%S ")))
        
        else:
            resultado_saida.append("{0} zica".format(endereco_consultado))
        
        parametro_fila.task_done()


#Leia o arquivo de entrada
lista_de_enderecos = open("arquivo_entrada.txt", "r").readlines()

#Gerando o pacote de threads
for contador in range(numero_threads):

    minha_thread = Thread(target=meu_verificador, args=(contador, fila_de_threads))
    minha_thread.setDaemon(True)
    minha_thread.start()

#enfilera cada thread na variavel fila_de_threads
for endereco_atual in lista_de_enderecos:
    fila_de_threads.put(endereco_atual)

#espera as threads terminarem para sair    
fila_de_threads.join()

with open('arquivo_saida.txt', 'a') as ponteiro_arquivo_saida:
    for r in resultado_saida:
        ponteiro_arquivo_saida.write(r + "\n")

# Referências
# http://sharats.me/the-ever-useful-and-neat-subprocess-module.html
# http://stackoverflow.com/questions/32364849/what-difference-between-subprocess-call-and-subprocess-popen-makes-pipe-less

