
#read the file with SeqIO

from Bio import SeqIO

for record in SeqIO.parse("dna.fasta", "fasta"):
    print(record.id, len(record.seq), record.seq[:10]) 


#reverse complements 

from Bio.SeqRecord import SeqRecord

rc_records = []
for record in SeqIO.parse("dna.fasta", "fasta"):
    rc_seq = record.seq.reverse_complement()
    rc_record = SeqRecord(
        rc_seq,
        id=record.id + "_rc",
        description="reverse complement of " + record.id,
    )
    rc_records.append(rc_record)

SeqIO.write(rc_records, "dna_rc.fasta", "fasta")



#GC% annotation

gc_records = []
for record in SeqIO.parse("dna.fasta", "fasta"):
    seq = str(record.seq)
    gc = 100 * (seq.count("G") + seq.count("C")) / len(seq)
    gc = round(gc, 1)
    gc_record = SeqRecord(
        record.seq,
        id=record.id,
        description="GC=" + str(gc) + "%",
    )
    gc_records.append(gc_record)

SeqIO.write(gc_records, "dna_with_gc.fasta", "fasta")

#translation 

print("Translation:")
for record in SeqIO.parse("dna.fasta", "fasta"):
    protein = record.seq.translate()
    print(record.id, protein[:10])

print("Check dna_rc.fasta:")
for record in SeqIO.parse("dna_rc.fasta", "fasta"):
    print(record.id, "|", record.description)