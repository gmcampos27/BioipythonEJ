from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

myseq = Seq("ATCG")

print(type(myseq))

ref = Seq("AAACGATATTAGACGACGCTACTAGTTA")

#Contando

concat = myseq + ref

a_count = myseq.count('A')
c_count = myseq.count('C')
g_count = myseq.count('G')
t_count = myseq.count('T')

tamanho = len(myseq)

print(tamanho)

print(a_count)
print(c_count)
print(g_count)
print(t_count)

GC_content = gc_fraction(myseq)
print(GC_content)

print(myseq.count("AA"))

for base in myseq:
    if base == "A":
        print("Adenina")

contigs = [Seq("AAAA"), Seq("TTT"), Seq("GGGG")] #preciso preencer
spacer = Seq("N"*5)

scaffold = spacer.join(contigs)

print(scaffold)