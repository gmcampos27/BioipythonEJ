from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction
import glob

'''
#genomas completos e incompletos

record = SeqIO.read("genoma_completo.fna.txt", "fasta")

print(record.id)

print(record.name)

print(record.description)

#print(record.seq)

print(len(record.seq))

print(record.seq.count("A"))

print(gc_fraction(record.seq))


#record = SeqIO.parse("genoma_completo.fna.txt", "fasta")

identifier = [seq_record.id for seq_record in SeqIO.parse("genoma_completo.fna.txt", "fasta")]

print(identifier) #se for completo vai ter 1 id, caso contrário, mais


for file in glob.glob("*.fna"):
    for seq_record in SeqIO.parse(file, "fasta"):
        print(file, seq_record.id)

# for seq_record in SeqIO.parse("genoma_incompleto.fna", "fasta"):
#     contig = seq_record.id    
#     print(f"Esse é o contig {contig}")

'''
#arquivos multifasta

lista = []

for seq_record in SeqIO.parse("todos.fasta", "fasta"):
    desc = seq_record.description
    desc = desc.split('UNVERIFIED:')
    #lista.append(seq_record.description)
    print(desc)

'''
with open("teste.txt", "w") as arquivo:
    for iten in lista:
        arquivo.write(iten + '\n')
'''