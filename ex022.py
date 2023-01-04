nome = str(input('Digite seu nome: ')).strip()

print('seu nome em maiusculo é {}'.format(nome.upper()))

print('Seu nome em minusculo é {}'.format(nome.lower()))

print('seu nome tem {} letras' .format(len(nome)-nome.count(' ')))

print('seu primeiro nome tem {} letras' .format(nome.find(' ')))