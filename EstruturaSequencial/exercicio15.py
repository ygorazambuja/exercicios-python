print('Valor recebido por hora')
valorRecebidoHora = float(input())

print('Horas Trabalhadas no Mês')
horasTrabalhadas = int(input())

salario = valorRecebidoHora * horasTrabalhadas
print('Salario Bruto = {}'.format(salario))

impostoRenda = salario * 0.11
print('IR = R${}'.format(impostoRenda))

inss = salario * 0.08
print('INSS = R${}'.format(inss))

sindicato = salario * 0.05
print('Sindicato R${}'.format(sindicato))

salarioLiquido = salario - impostoRenda - inss - sindicato
print('Salario Liquido R${}'.format(salarioLiquido))
