print('João Papo-de-Pescador')
kilosPeixe = int(input('Kilos de Peixe'))

excesso = kilosPeixe - 50
if(excesso <= 0):
    print('não tem kilos excedente')
else:
    print('Kilos excedentes = {}, vai pagar R${} de multa'.format(
        excesso, (excesso*4)))
