x = str(input('Digite seu nome completo: ')).strip()
y = x.split()

print('Seu primeiro nome é {}' .format(y[0]))
print('Seu ultimo nome é {}' .format(y[len(y)-1]))
