#!/usr/bin/python

import subprocess
try:
    #imprime o resultado e mescla stdout e std
    resultado = subprocess.check_output("echo o nome do usuario eh ${USER} ", stderr=subprocess.STDOUT, shell=True)
    print resultado
    #causa erro e mescla stdout e stderr
    resultado = subprocess.check_output("copy asdfjaefda", stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError, deu_erro: # Codigo de erro <> 0 
    print "--------erro------"
    print deu_erro.cmd
    print deu_erro.message
    print deu_erro.returncode
    print deu_erro.output # contem stdout e stderr  
