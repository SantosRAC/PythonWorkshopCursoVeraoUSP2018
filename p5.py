import sys

a = sys.argv[1]

f = open(a)

x=1
for i in f:
	if((x%2)==0):
		print(i, end="")
	x=x+1
