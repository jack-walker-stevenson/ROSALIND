from sys import argv

script, seq = argv

CODON_TO_AA = {'UUU': 'F',     'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
               'UUC': 'F',     'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
               'UUA': 'L',     'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
               'UUG': 'L',     'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
               'UCU': 'S',     'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
               'UCC': 'S',     'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
               'UCA': 'S',     'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
               'UCG': 'S',     'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
               'UAU': 'Y',     'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
               'UAC': 'Y',     'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
               'UAA': 'Stop',  'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
               'UAG': 'Stop',  'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
               'UGU': 'C',     'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
               'UGC': 'C',     'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
               'UGA': 'Stop',  'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
               'UGG': 'W',     'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}

if len(seq) > 10000:
    raise ValueError("sequence too long")

# split sequence into list of codons after trimming trailing bases
mod = len(seq) % 3
if mod != 0:
    seq = seq[:-mod]
codons = [seq[i:i+3] for i in range(0, len(seq), 3)]
# translate entire sequence, then print just portion before first stop
print(''.join([CODON_TO_AA[c] for c in codons]).split("Stop")[0])
