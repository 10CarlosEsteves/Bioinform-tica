# Escreva um programa que leia um arquivo multi-fasta e 
# armazene em um dicionário: cabeçalho da sequência como 
# a chave e a sequência como valor.

#chave = re.findall(">[A-Z]+_[0-9]+",file)
#porta = re.split(">[(A-Z)+_(0-9)+]",file)

import re
arquivo = open("virus.FASTA", "r")
file = arquivo.read()

chave = re.findall(">[A-Z]+_[0-9]+",file)
porta = re.split(">[A-Z]+_[0-9]+",file)

biblioteca = {}

for i in range(0,5):

    biblioteca[chave[i]] = porta[i+1]

X = input("Por favor insira a chave: ")

print(biblioteca[X])





