from Bio import Entrez

'''
Entrez.email = "gabrielmdecampos@usp.br"

handle = Entrez.einfo()

result = Entrez.read(handle)

print(result)

'''

'''
Entrez.email = "gabrielmdecampos@usp.br"

#Carregar a info
handle = Entrez.efetch(db = "nucleotide", id="NZ_CP041838.1", rettype = "fasta", retmode = "text")
#Acession Number
#rettype = tipo de arquivo (fasta)

with open("NZ_CP041838.1.fasta", "w") as arquivo:
    arquivo.write(handle.read())
handle.close()


handle = Entrez.efetch(db = "nucleotide", id="NZ_CP041838.1", rettype = "gbwithpaths", retmode = "text")
#Acession Number
#rettype = tipo de arquivo (fasta)

with open("NZ_CP041838.1.gbff", "w") as arquivo:
    arquivo.write(handle.read())
handle.close()

'''

#Baixar vários
#Usa o assecion number

Entrez.email = "gabrielmdecampos@usp.br"

genome_ids = []

with open("ids.txt") as arquivo:
    genome_ids = arquivo.readlines()
    print(genome_ids)

new_lst = []

for i in genome_ids:

   genome_id = i.strip()
   
   handle = Entrez.efetch(db = "nucleotide", id=genome_id, rettype = "fasta", retmode = "text")
   
   with open(f"{genome_id}.fasta",  "w") as arquivo:
        arquivo.write(handle.read())
   handle.close()
   
   handle = Entrez.efetch(db = "nucleotide", id="NZ_CP041838.1", rettype = "gbwithpaths", retmode = "text")

   with open(f"{genome_id}.gbff",  "w") as arquivo:
        arquivo.write(handle.read())
   handle.close()

   print(f"Arquivos FASTA e GBFF para o genoma {genome_id} baixados com sucesso")
