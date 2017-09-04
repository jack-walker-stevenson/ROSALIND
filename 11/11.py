from sys import argv
from Bio import SeqIO, SeqUtils

script, filename = argv
records = SeqIO.parse(filename, "fasta")

relevant = tuple((record.id, SeqUtils.GC(record.seq)) for record in records)

maxgc = max(relevant, key=lambda x: x[1])
print(maxgc[0] + "\n" + str(maxgc[1]))
