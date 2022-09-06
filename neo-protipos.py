import os
from Bio import SeqIO

os.system("clear")
nome = str(input("Por favor insira o nome do arquivo que deseja abrir:"))

#Manipulando o arquivo para um dicionário
records = SeqIO.to_dict(SeqIO.parse(nome, "fasta"))


comando = int(1)
while(comando):
    os.system("clear")
    X = input("Por favor insira a chave para acessar o conteudo: ")
    
    print("\n>",records[X].description)
    print(records[X].seq)
    comando=int(input("\nDeseja rodar o programa novamente?\n [1]SIM [NAO]\n>"))

print("Programa encerrado!")
