idades=[]
sexo=[]
nome=[]
for i in range(4):
    nomes= (input('qual seu nome?'));
    nome.append(nomes)
    idade=int(input('quantos anos voçê tem?'))
    idades.append(idade)
    m=m+idade
    sex=input('digite seu sexo')
    sexo.append(sex)
print('a média das idades é', m/4)


