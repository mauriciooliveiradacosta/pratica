n=[]
s=0
for i in range(6):
    N=int(input('digite um número'))
    n.append(N)
    if N%2==0:
        s+=N
print ('a soma dos números pares é',s)