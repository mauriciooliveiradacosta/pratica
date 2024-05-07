def position(p):
    f=[0]* p
    n=1
    for i in range(p):
        f[i]=n
        n=n +f[i-1]
    return(f)
v=int(input("digite a posição de p:"))
print(position(v))