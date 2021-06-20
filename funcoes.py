import os
from datetime import date

def Logs(nome, email):
    dataAtual = date.today()
    arquivo = open("LogJogoEducacional.txt", "a")
    arquivo.write(f"Data: {dataAtual} - Nome: {nome} - E-mail: {email}\n")
    arquivo.close()