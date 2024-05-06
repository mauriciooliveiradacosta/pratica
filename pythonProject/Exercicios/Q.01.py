s=0
cont=0
for i in range(1,501,2):
    print(i)
for i in range(1,501,2):
   if i%3==0:
       cont += 1
       s += i
print('a soma dos {} números multiplos de 3 e que são impares  é {}' .format(cont, s))