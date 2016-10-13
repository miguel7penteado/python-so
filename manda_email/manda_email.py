#!/usr/bin/python    

from smtplib import SMTP
from smtplib import SMTP_SSL
from smtplib import SMTPException
from socket import error
import socket


import datetime
debuglevel = 0

nome_maquina = socket.gethostname()

carteiro = SMTP_SSL()
#carteiro = SMTP()
carteiro.set_debuglevel(debuglevel)

try:
	print "Conectando ao servidor de e-mail..."
	carteiro.connect('smtp.ibge.gov.br', 465)
except error, deu_erro:
    print "Erro na conexao: %s" % deu_erro
    
try:
	print "Fazendo o login..."
	carteiro.login('usuario', 'senha')
except SMTPException, mensagem_erro_carteiro:
    print "Erro de usuario ou senha: %s" % deu_erro


remetente = "Miguel Penteado <miguel.penteado@ibge.gov.br>"
destinatario = "<miguel.penteado@ibge.gov.br"
titulo = "Script python de envio de e-mail"
data_envio = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
print (data_envio)
corpo_mensagem = "Este h um e-mail gerado em python ASCII\n\n Script realizado com sucesso \nO nome da maquina eh %s." % (nome_maquina)

mensagem_com_cabecalho = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( remetente, destinatario, titulo, data_envio, corpo_mensagem )


try:
	carteiro.sendmail(remetente, destinatario, mensagem_com_cabecalho)
except SMTPException, deu_erro: 
    print "Erro:" % deu_erro

carteiro.quit()
