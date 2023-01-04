v = float(input('Digite a velocidade do veiculo: '))
m = (v - 80) * 7
if v <= 80:
    print('Você está dentro dos limites de velocidade')
else:
    print('Limite de velocidade excedido, você deverá pagar {:.2f} R$ de multa' .format(m))