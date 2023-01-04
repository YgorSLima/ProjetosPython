x = float(input('Digite a largura de sua parede:'))
y = float(input('agora digite a sua altura:'))
z = x*y
l = z/2

print('tendo em vista que cada litro de tinta pinta 2m² e sua parede possui uma area de {}m², você necessiatrá de {}L para pinta-la' .format(z, l))