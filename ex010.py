r = float(input('Vamos falar de economia? Me diz aí quantos R$ que você tem que eu te digo quantos dolares você conseguiria comprar: R$'))
d = r / 5.28


print('Seguindo a cotação do dolar feito no dia 15/12/2022 as 02:28 do horario de brasilia você consegueria comprar com {:.2f} Reias um total de U${:.2f} dolares' .format(r, d))