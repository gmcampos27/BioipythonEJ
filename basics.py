from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from Bio.Data import CodonTable
from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate

my_seq = Seq("ACCGTATTAGCC")

my_seq.count("G")
my_seq.count("C")

print(gc_fraction(my_seq))

my_seq[4:10]
my_seq[1::3]

my_seq.complement()

fasta_format_string = ">ficticio\n%s\n" % my_seq

print(fasta_format_string)

coding_dna =  Seq("ACCGTATTAG") #DNA

template_dna = coding_dna.reverse_complement() #mRNA 3' - 5'

messenger_rna = template_dna.reverse_complement().transcribe()  #mRNA 5' - 3'

messenger_rna.back_transcribe() #mRNA -> DNA

print(template_dna)

print(messenger_rna)

print(messenger_rna.translate())

print(coding_dna.translate(table="Vertebrate Mitochondrial"))

print(coding_dna.translate(table=2, stop_symbol="@"))


gene = Seq(
"GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
"GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
"AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
"TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
"AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA"
)
print(gene)

gene.translate(table="Bacterial")


standard_table = CodonTable.unambiguous_dna_by_id[1]
mito_table = CodonTable.unambiguous_dna_by_id[2]

print(standard_table)

my_string = "GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG"
print(reverse_complement(my_string))
print(transcribe(my_string))
print(translate(my_string))

record = SeqIO.read("NC_005816.fna", "fasta")
print(record)
