#Exercício 1

#Calcule o tamanho médio dos genes de vários genomas e armazenar em um arquiv

#Bibliotecas

from Bio import SeqIO
from Bio.Seq import Seq
import glob
from Bio.SeqUtils import gc_fraction


out = open("tamanhomedio.txt", "w")

for file in glob.glob("*.fna"):

    count = 0
    tam = 0
    media = 0

    for seq_record in SeqIO.parse(file, "fasta"):

        tam = tam + len(seq_record.seq)
        count = count + 1

    media = tam/count

    escreva = file + '\t' + str(media) + '\n'
    out.writelines(escreva)
out.close()


#Exercício 2

#Calcule o conteúdo de GC de vários genomas e escreva em um arquivo de saída o id do genoma, o nome da espécie, o tamanho do genoma em pb e o valor do conteúdo GC


out = open("genomas.txt", "w")

for file in glob.glob("*.fna"):
    for seq_record in SeqIO.parse(file, "fasta"):
         id = seq_record.description
         pb = len(seq_record.seq)
         gc = gc_fraction(seq_record.seq)
         escrever = id + '\t' + f"{pb} pares de base" + '\t' + '\t' + str(gc) + '\n'
         out.writelines(escrever)
out.close()



#Exercício 3

#Crie primers de 15 nucleotídeos da porção inicial de cada gene da fita senso, com exceção dos pseudogenes e armazene-os em um arquivo

out = open("primers.txt", "w")

for file in glob.glob("genes.fna"):
    for seq_record in SeqIO.parse(file, "fasta"):
        if 'pseudo=true' not in seq_record.description and 'complement' not in seq_record.seq:
            primer = seq_record.seq[0:15]
            id = seq_record.id
            escrever = id + '\t' f"{primer}" + '\n'
            out.writelines(escrever)
out.close()

