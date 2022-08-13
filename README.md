# Bioinform-tica
(PTBR)
Repositório contendo programas de bioinformática em Python oriundos de exercícios ou projetos

NOTA prototipo.py:

Código oriundo de exercicio. Basicamente o código precisa estar em um diretório(pasta) junto com uma arquivo .fasta para funcionar melhor, o programa funciona com arquivos fasta contendo varias contigs ou sequencias com varios cabeçalhos de genes ou proteinas. O progama pedirá para inserir o nome do arquivo e depois, automaticamente, ele vai separar o arquivo de cabeçalhos e conteudos para "chave" e "porta" de dicionários, assim uma vez concluido, voce pode acessar o conteudo de determinada sequencia apenas informando o cabeçalho(do caractere ">" até o ultimo numero). Futuramente servirá como base para outros programas e manipulação de arquivos .fasta complexos.


(ENGB)

NOTE prototipo.py:

This is a code from a exercise. Basically the code needs to be in a directory(folder) with a .fasta extension file, the program works with a fasta file that contains many genes and proteins sequences separeted with contigs or headers. The program will ask for the name of the fasta file, you should inform the hole file name. When the process begin, 2 lists will be genereted, one contains the headers and other the nucleotide or aminoacid sequence, both lists will be part of an dictionary called "library" the headers will be the key and sequence the value. After the processes finish it will ask for the key, you should insert the header(from the ">" caractere until the last number, gene or aminoacid name are not necessary). Futhermore this program will be a base for more complex programs and .fasta file manipulating.
