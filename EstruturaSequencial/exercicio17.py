from math import ceil


metroQuadrados = int(input('Metros Quadrados: '))
litrosTinta = ceil(metroQuadrados * 0.16)
quantidadeLatas = litrosTinta / 18
quantidadeGaloes = litrosTinta / 3.6

print('Precisaremos de {:.2f} litros de Tinta'.format(litrosTinta))
print('Quantidade Galoẽs:  {:.2f}   Quantidade Latas: {:.2f}'.format(
    quantidadeGaloes, quantidadeLatas))

print('Preço comprando apenas latas de 18 litros:  R${}'.format(
    ceil(quantidadeLatas) * 80))
print('Preço comprando apenas Galões de 3,6 litros:  R${}'.format(
    (ceil(quantidadeGaloes) * 25)))

precoMisturado = 0
while litrosTinta >= 18:
    precoMisturado = precoMisturado + 80
    litrosTinta = litrosTinta - 18
    pass

while litrosTinta > 0:
    precoMisturado = precoMisturado + 25
    litrosTinta = litrosTinta - 3.6
    pass

print(litrosTinta)
print('Preço misturando Latas e Galões : R${}'.format(precoMisturado))
