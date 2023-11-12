#criando dicionarios

dicionario = {}

dicionario = dict()


dicionario = { 'nome': 'Leo', 'idade':28 ,'altura':1.86}

print(dicionario)
print(dicionario['idade'])


#adicionando itens no dicionario

dicionario [ 'programador'] = True
#sobreescrevendo valor de altura no meu dicionario
dicionario ['altura'] = 2


#iterando um dicionario 

for chave in dicionario:
    print(chave,":", dicionario[chave])

# testando se um a chave existe no dicionario

print('peso' in dicionario)
print ('altura'in dicionario)

