d = int(input('Quantidade de dias que você alugou o veiculo:'))
km = float(input('Quantidade de Km rodados:'))
x = d * 60
y = km * 0.15
v = x + y

print('O valor a pagar é de R$:{:.2f}'.format(v))