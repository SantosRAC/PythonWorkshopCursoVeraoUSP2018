import sys
from collections import Counter

a = sys.argv[1]

f = open(a)

### Coloca o arquivo em uma linha
x = f.read().split(" ")

### Exclui o '\n'
x[len(x)-1] = x[len(x)-1].rstrip()

### Cria dicionario
x = Counter(x)

for key, value in x.items():
	print(key, "", end="")
	print(value)
