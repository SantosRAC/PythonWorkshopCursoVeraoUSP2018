import sys

texto = sys.argv[1]
partes = [int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]), int(sys.argv[5])]

print(texto)
print(partes[1])

print("Resultado:\n", texto[partes[0]:partes[1]+1], texto[partes[2]:partes[3]+1]) 

#### Run on terminal:
## python p3.py JD4jyKuwUjq1D88jp3Sf5LJ1cjZWj5c0HnUk1X9i3CnBrNM5T989nUorXFznKpkyYWAlaussLOXKMbI8Z9d7JCIREs7NGlCLkCUR1MUy4Tp99yCc1Ps0sqHhp2eycS0da1hIheUwA8Y1tzdriULS9aDqm2hXj1BtfyVWSwYalbocinctusD. 66 70 167 177
