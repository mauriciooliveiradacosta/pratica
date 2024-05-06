def fibo (q):
    n=1
    v=[0]*q
    for i in range (0,q):
        v[i]=n
        n= n+v[i-1]
    return v
Q=int(input('digite o limite de valores'))
print(fibo(Q))
