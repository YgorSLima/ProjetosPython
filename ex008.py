m = int(input('digite uma distancia em metros:'))
dam = m/10
hm = dam/10
km = hm/10
dm = m*10
cm = dm*10
mm = cm*10

print('esta distencia é o equivalente a: \n {}dm \n {}cm \n {}mm \n{}dam \n{}hm \n{}km' .format(dm, cm, mm, dam, hm, km))