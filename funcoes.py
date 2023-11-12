def saudacao():
    print('seja bem vindos')
    print('é um prazer ver voce iniciando neste curso')





#funcoes com parametros

def saudacao(nome, curso):
    print(f'seja bem vindo {nome}!')
    print(f'é um prazer ver voce iniciando no curso de {curso}')

saudacao('leonardo', 'python')

#funcoes com parametros default

def saudacao(nome, curso= 'python'):
    print(f' seja bem vindo {nome} !')
    print(f'é um prazer ter voce conosco no curso de {curso}')


saudacao('leonardo')


# funcoes com retorno
"""
#o ' return ' dentro de função faz com que o código abaixo dele seja ignorado, então
só utilize o return no final da sua função"""


def soma(num1, num2):
    return num1 + num2 
resultado = soma(2,5)

print('o resultado da soma é ', resultado)

def calculadora(num1, num2, operação = "+"):
    if operação == '+':
        return num1 + num2
    elif operação == '-':
        return num1 - num2
    elif operação == '*':
        return num1 * num2
    elif operação == '/':
       return num1 / num2
    else:
        print('insira um operador válido para o calculo.') 

valores = calculadora(2,5,'a')

print('o resultado da sua calculadora é ', valores)


