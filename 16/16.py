from sys import argv

_, filename = argv
fasta = open(filename).read()  # yeah, open with, but nothing here but file ops
# extract sequences from FASTA file
seqs = [s.split('\n')[1] for s in fasta.split('>')[1:]]
seq_len = len(seqs[0])  # assume size invariants
a = [0] * seq_len
c = [0] * seq_len
g = [0] * seq_len
t = [0] * seq_len
for seq in seqs:
    for i, base in enumerate(seq):
        if base == a:
            a[i] += 1
        elif base == c:
            c[i] += 1
        elif base == g:
            g[i] += 1
        elif base == t:
            t[i] += 1
consensus = ''
for i, bases in enumerate(zip(a, c, g,t)):

print(consensus)
print("A: " + ' '.join[a])
print("C: " + ' '.join[c])
print("G: " + ' '.join[g])
print("T: " + ' '.join[t])
