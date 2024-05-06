v= [0] *15
maior= v[0]
menor= v[0]
for i in range (0,15):
    v[i]=float (input("digite a altura"))
    if v[i]>maior:
        maior=v[i]
    elif v[i]<menor:
        menor=v[i]
print('o maior valor foi ',maior)
print('o menor valor foi ',menor)
