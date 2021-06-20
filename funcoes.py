import random
from datetime import date

def Logs(nome, email):
    dataAtual = date.today()
    arquivo = open("LogJogoEducacional.txt", "a")
    arquivo.write(f"Data: {dataAtual} - Nome: {nome} - E-mail: {email}\n")
    arquivo.close()

def Vogal():
    vogais = ['A', 'E', 'I', 'O', 'U']
    vogalAleatoria = vogais[random.randint(0,4)]
    return vogalAleatoria

def Consoante():
    consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']
    consoanteAleatoria = consoantes[random.randint(0, 18)]
    return consoanteAleatoria