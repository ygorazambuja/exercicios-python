nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1+nota2) / 2

if(media == 10.0):
    print('Aprovado com Distinção com a nota {}'.format(media))

elif(media > 7):
    print('Aprovado com a nota {}'.format(media))

elif(media < 7):
    print('Reprovado com a nota {}'.format(media))
