from math import ceil
metroQuadrados = int(input('Metros Quadrados: '))
litrosTinta = ceil(metroQuadrados * 0.33)
quantidadeLatas = litrosTinta / 18
print('Sera necessario uma quantidade de {:.2f} litros de tinta, custando no total {:.2f}'.format(
    quantidadeLatas, (quantidadeLatas * 80)))
