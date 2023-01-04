km = float(input('digite  a quantidade de km tem sua viagem: '))
if km <= 200:
    v = km * 0.50
    print('O valor da sua viagem é de {:.2f} R$' .format(v))
else:
    vp = km * 0.45
    print('O valor da sua viagem é de {:.2f} R$'.format(vp))