from sys import argv

script, filename = argv
seqs = open(filename).read().split("\n")
comp = zip(seqs[0], seqs[1])
count = 0
for (a, b) in comp:
    if a != b:
        count += 1
print(count)
