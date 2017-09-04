from sys import argv

script, n, k = argv
n = int(n)
k = int(k)

if n > 40 or n < 0 or k > 5 or k < 0:
    raise ValueError("invalid input")
else:
    pairs = 1
    immature_pairs = 0
    while n > 1:
        maturing = immature_pairs
        immature_pairs = k * pairs
        pairs = pairs + maturing
        n -= 1
    print(pairs)
