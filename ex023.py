n = int(input('informe um numero até 9999:'))

u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10

print('o numero de unidades é {}' .format(u))
print('o numero de dezenas é {}' .format(d))
print('o numero de centenas é de {}' .format(c))
print('o numero de milhar é de {}' .format(m))
