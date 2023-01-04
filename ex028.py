from random import randint
from time import sleep
pc = randint(0, 5)
user = int(input('tente adivinhar um numero de 0 a 5 escolhido pelo computador: '))
print('AGUARDE O RESULTADO')
sleep(2.3)
if user == pc:
    print('parabens, você acertou! O numero de fato era {}' .format(pc))
else:
    print('Você errou, tente novamente!')



