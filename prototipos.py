# Escreva um programa que leia um arquivo multi-fasta e 
# armazene em um dicionário: cabeçalho da sequência como 
# a chave e a sequência como valor.

#chave = re.findall(">[A-Z]+_[0-9]+",file)
#porta = re.split(">[(A-Z)+_(0-9)+]",file)

import re
import os
os.system("clear")
nome = input("Por favor insira o nome do arquivo que deseja abrir:")

arquivo = open(nome, "r")
file = arquivo.read()

chave = re.findall(">[A-Z]+_[0-9]+",file)
porta = re.split(">[A-Z]+_[0-9]+",file)

biblioteca = {}

for i in range(0,5):

    biblioteca[chave[i]] = porta[i+1]

comando = int(1)

while(comando):
    os.system("clear")
    X = input("Por favor insira a chave para acessar o conteudo: ")

    print(biblioteca[X])
    comando=int(input("\nDeseja rodar o programa novamente?\n [1]SIM [NAO]\n>"))

print("Programa encerrado!")
