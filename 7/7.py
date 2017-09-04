from sys import argv

script, filename = argv
dna = open(filename).read()

if len(dna) > 1000:
    raise ValueError("Sequence longer than 1 kb")
else:
    a = dna.count("A")
    c = dna.count("C")
    g = dna.count("G")
    t = dna.count("T")
    print("{} {} {} {}".format(a, c, g, t))
