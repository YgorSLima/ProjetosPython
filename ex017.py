from math import hypot
co = float(input('digite o valor do cateto oposto:'))
ca = float(input('digite o valor do cateto adjacente:'))
hi = hypot(co, ca)
'''hi = (co ** 2 + ca ** 2) ** 0.5'''

print('O valor da hipotenusa é:{:.2f}' .format(hi))