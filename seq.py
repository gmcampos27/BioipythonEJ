from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from Bio.Data import CodonTable
from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate
from Bio.SeqFeature import SeqFeature, SimpleLocation

record = SeqIO.read(r"C:\Users\USUARIO\Dropbox\PC (3)\Documents\Python\Biopython\NC_005816.fna.txt", "fasta")
print(record)

print(record.id)
print(record.name)

seq = Seq("ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTTCCTTCCTGCCAGTGCTGAGGAACTGGGAGCCTAC")

feature = SeqFeature(SimpleLocation(5, 18, strand=-1), type="gene")
print(feature)

record_gb = SeqIO.read(r"C:\Users\USUARIO\Dropbox\PC (3)\Documents\Python\Biopython\NC_005816.gb", "genbank")

print(record_gb)
len(record_gb.features)
print(record_gb.features[2])
