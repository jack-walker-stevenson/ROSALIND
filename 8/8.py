from sys import argv

script, filename = argv
dna = open(filename).read()

if len(dna) > 1000:
    raise ValueError("Sequence longer than 1 kb")
else:
    print(str.replace(dna, 'T', 'U'))
