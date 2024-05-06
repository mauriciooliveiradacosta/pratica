n=1
c=int(input('digite um número'))
v=[0]*c
for i in range (0,c):
    v[i]=n
    n=n+v[i-1]
print(v)


