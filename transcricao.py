from Bio.Seq import Seq

codificante = Seq("ATGG") #5' 3'
molde = Seq("CCAT") #eh 3' 5', mas vemos como se fosse 5' 3'

#Transcrição direta (bioinfo)
mRNA_cod = codificante.transcribe() #não precisa da molde
print(mRNA_cod)

mRNA_cod_python = codificante.replace("T", "U") #essa q é a "função"

#Na vida real

mRNA_molde = molde.reverse_complement().transcribe()
print(mRNA_molde)

#Transcrição Reversa

mRNA = Seq("AUUGGCUAACAAGAGCGAGCGUACGAUGCUAAC")
dna = Seq("GTGGGCTAG")
print(len(mRNA))

#Tradução

prot1 = dna.translate(to_stop=False, cds= True, table= "Bacterial")
prot2 = dna.translate(table="Vertebrate Mitochondrial")

print(prot1)
print(prot2)