from Bio import SeqIO
from Bio.Seq import Seq

print("---------------------------------------------------------------------------")
i_file = str(input("User, please, insert the full name of your multifasta file: "))
o_file = str(input("Now, give the translated output file a name: "))

input_file =  open(i_file,"r+")
output_file = open(o_file,"a")

lines = input_file.readlines()
number = int(0)

for line in lines:

    words = str(line)

    if words[0] == '>':

         output_file.write(words)
         number = int(0)
        
    else:
        number +=1
        DNA = Seq(words)
        aminoacid = DNA.translate()
        aminoacid = str(aminoacid)
        aminoacid = aminoacid.replace('*',"")
        output_file.write(aminoacid)
        
        if number%3==0:
            output_file.write("\n")

        elif len(aminoacid)<20:
            output_file.write("\n")

print("---------------------------------------------------------------------------")
print("Transalation succesfully concluded, open the %s file to see the results" %o_file,)
