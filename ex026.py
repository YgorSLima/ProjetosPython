x = str(input('Digite uma frase: ')).lower().strip()
print('A letra A pareceu {} vezes' .format(x.count('a')))
print('A primeira letra A apareceu na posição {}' .format(x.find('a')))
print('a ultima letra A apareceu na posição {}' .format(x.rfind('a')))