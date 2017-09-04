from sys import argv


def _complement(c):
    if c == 'A':
        return 'T'
    elif c == 'T':
        return 'A'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'
    elif c == '\n':
        return ''
    else:
        raise ValueError("invalid base")

script, filename = argv
dna = open(filename).read()

if len(dna) > 1000:
    raise ValueError("Sequence longer than 1 kb")
else:
    comp = list(map(_complement, dna))
    list.reverse(comp)
    print(''.join(comp))
