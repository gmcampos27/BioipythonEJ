from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import glob



for file in glob.glob("*.fna"):
    out = open(file.replace(".fna","_OUT.fasta"), "w")
    for seq_record in SeqIO.parse("cds_from_genomic.fna", "fasta"):
        if 'pseudo=true' in seq_record.description:
            myseq = seq_record.seq
            gene = SeqRecord(myseq, id = seq_record.id, description= seq_record.description)

            SeqIO.write(gene, out, "fasta")
    out.close()

'''
myseq = Seq("ACGTAGACTCGATCTTGA")
gene = SeqRecord(myseq,id="gene_id_1", description= "Descrição do gene 1")

SeqIO.write(gene, "output.fna", "fasta")

'''