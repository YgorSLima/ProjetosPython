from random import choice
a1 = input('Digite o primero nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceito nome: ')
a4 = input('Digite o quarto nome: ')

list = [a1, a2, a3, a4]
e = choice(list)

print('O nome escolhido foi: {}' .format(e))