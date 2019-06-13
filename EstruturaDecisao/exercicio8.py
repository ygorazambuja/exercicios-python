numero1 = float(input('Preço produto 1: '))
numero2 = float(input('Preço produto 2: '))
numero3 = float(input('Preço produto 3: '))

if(numero1 < numero2 and numero1 < numero3):
    print('Produto 1 é o mais barato: {}'.format(numero1))
elif(numero2 < numero1 and numero2 < numero3):
    print('Produto 2 é o mais barato: {}'.format(numero2))
elif(numero3 < numero1 and numero3 < numero2):
    print('Produto 3 é o mais barato: {}'.format(numero3))
