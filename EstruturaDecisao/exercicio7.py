numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
numero3 = int(input('Numero 3: '))

if(numero1 < numero2 and numero1 < numero3):
    print('Numero 1 é o menor: {}'.format(numero1))
elif(numero2 < numero1 and numero2 < numero3):
    print('Numero 2 é o menor: {}'.format(numero2))
elif(numero3 < numero1 and numero3 < numero2):
    print('Numero 3 é o menor: {}'.format(numero3))
