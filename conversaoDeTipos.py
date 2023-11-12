soma = 0

for i in range (1,4):
    nota = float(input(f'informe a sua nota {i}:' ))

    soma = soma + nota
    
print(soma)
media = soma/i
print(media)