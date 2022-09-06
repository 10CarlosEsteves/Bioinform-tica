# Bioinform-tica
-----------------------------------------------------------------------------------------------------------------------------------------------------------
(PTBR)
Repositório contendo programas de bioinformática em Python oriundos de exercícios ou projetos

NOTA prototipo.py:

Código oriundo de exercicio. Basicamente o código precisa estar em um diretório(pasta) junto com uma arquivo .fasta para funcionar melhor, o programa funciona com arquivos fasta contendo varias contigs ou sequencias com varios cabeçalhos de genes ou proteinas. O progama pedirá para inserir o nome do arquivo e depois, automaticamente, ele vai separar o arquivo de cabeçalhos e conteudos para "chave" e "porta" de dicionários, assim uma vez concluido, voce pode acessar o conteudo de determinada sequencia apenas informando o cabeçalho(do caractere ">" até o ultimo numero). Futuramente servirá como base para outros programas e manipulação de arquivos .fasta complexos.


NOTA neo-prototipo.py:
O código prototipo.py foi reescrito e aprimorado sob o nome neo-prototipo.py. O funcionamento é igual, apenas utilizamos uma função do Biopython, o SeqIo, para tornar o processo mais eficaz. 


NOTA fasta_translator.py:

Este código tem como propósito servir de exemplo para projetos futuros. O código basicamente é um tradutor de arquivos multifasta, ele pega um arquivo contendo várias cabeçalhos e sequencia de nucleotideos, faz a distinção entre eles e traduz as sequencias para aminoácidos e devolve a saída para um arquivo. Para melhorar a eficácia do programa é recomendado que seja executado em um diretório  a parte contendo o programa e o arquivo multifasta, o programa começa pedindo para o usuário digitar o nome completo do arquivo multifasta e em seguida pedirá para dar um nome para o arquivo em que será posto as sequencias traduzidas, após isso, o processo de tradução acontecerá e o resultado vai estar gravado no arquivo que voce deu o nome. Embora curto, esse código será de extrema importancia no desenvilmento de ferramentas futuras.

-----------------------------------------------------------------------------------------------------------------------------------------------------------
(ENGB)

NOTE prototipo.py:

This is a code from a exercise. Basically the code needs to be in a directory(folder) with a .fasta extension file, the program works with a fasta file that contains many genes and proteins sequences separeted with contigs or headers. The program will ask for the name of the fasta file, you should inform the hole file name. When the process begin, 2 lists will be genereted, one contains the headers and other the nucleotide or aminoacid sequence, both lists will be part of an dictionary called "library" the headers will be the key and sequence the value. After the processes finish it will ask for the key, you should insert the header(from the ">" caractere until the last number, gene or aminoacid name are not necessary). Futhermore this program will be a base for more complex programs and .fasta file manipulating.


NOTE neo-prototipo.py:

The code "prototipo.py" has been rewriten under the name "neo-prototipo.py". The behavior of the code is the same of his predecessor, we just make use of a Biopython's function, SeqIO, to make the process more efficient.


NOTE fasta_translator.py:

This code has the porpose of being an example for next projects. The code basically is a multifasta file translator, he will take an file that contains many headers and nucleotide sequence, he will separated them and translate the nucleotide into a aminoacid sequence and save the output in another file. To avoid troubles that may occur during the running, please execute this code in an separated directory with the multifasta file. When the program beggins, it will ask for the multifasta full name and after it will ask to give a name for the output translated file, feel free to give any name. After that, the translation process will begin and the results will be written in the output file. althought simple and short, this will be an base for next projects and other bioinformatics tools 
