import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def somaImpar(a, b):
	soma=0	
	for i in range(a, b):
		if(i%2==1):
			soma = soma + i
	return(soma)	


print(somaImpar(a,b))


##### Como usar:
### No terminal, digitar a linha seguinte substituindo os valores n1 e n2:
### python p2.py n1 n2

