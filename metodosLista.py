lista = [1, 15, 16, 17, 22, 23]


print(lista)

lista.append(3)

print(lista)
# o insert ele nao repoe o item, ele coloca outra coisa no lugar e joga o indice inicial pra frente
#exemplo, indice 2 começa com 12, ele joga o indice 2 para o 3 e coloca o valor de insert no 2
lista.insert(2, 10)

print("depois do insert", lista)

#extend

lista2 = [1,2,3]

lista.extend(lista2)
print(lista)

#pop

lista.pop()

print("lista apos o pop", lista)

lista.pop(0)

print("lista com um indice pop",lista)

lista.remove(1)

print(' lista depois de remover um parametro 1', lista)

#nota: o .remove só remove o primeiro item com os parametros solicitados, se vc tiver mais de um igual
#nao removerá todos

for i in range(0,2):
    lista.append(2)

print(lista)

#count 

print('quantidade de numero 2 na lista',lista.count(2))

#index
lista.append(12)
print('indice do elemento 12:', lista.index(12))

#organizador de lista em ordem crescente
lista.sort()

print(lista)

#reverse = true, organiza a lista de forma decrescente
lista.sort(reverse=True)

print(lista)

print(len(lista))