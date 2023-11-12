notas = [7.0, 15.0, 15.5]
print(len(notas))
lista_de_listas = [ 10, [1,2,3]]

lista = [10, ' leonardo ', 3.12444, False]

print(lista[3])


testeLista = []

testeLista.append(int(input("Insira sua idade: ")))
testeLista.append(input("Insira seu nome: "))
testeLista.append(float(input("Insira sua altura: ")))
print (testeLista)

if (testeLista[0] >= 25):
    print(f"{testeLista[1]} é Maior de 24 anos e tem {testeLista[2]} de altura")
else:
    print("f{testeLista[1]} é Menor de 24 anos e tem {testeLista[2]} de altura")

