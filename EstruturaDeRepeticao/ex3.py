

def validarNome(nome):
    if(not (len(nome) > 3)):
        print('Nome menor do que 3 caracteres')
        return False
    else:
        print('Nome maior do que 3 caracteres')
        return True
    pass


def validarIdade(idade):
    if(idade > 0 and idade <= 150):
        print('Idade Válida')
        return True
    else:
        print('Idade Inválida')
        return False
    pass


def validaSalario(salario):
    if(salario > 0):
        print('Salario Válido')
        return True
    else:
        print('Salario Invalido')
        return False
    pass


def validaSexo(sexo):
    if(sexo == 'f' or sexo == 'm'):
        print('Sexo valido')
        return True
    else:
        print('Sexo invalid')
        return False

    pass


def validaEstadoCivil(estadoCivil):
    if(estadoCivil == 's' or estadoCivil == 'c' or estadoCivil == 'v' or estadoCivil == 'd'):
        print('Estado civil válido')
        return True
    else:
        print('Estado civil Inválido')
        return False
    pass


if __name__ == "__main__":
    print('Nome: ')
    validarNome(input())
    print('Idade: ')
    validarIdade(int(input()))
    print('Salario:')
    validaSalario(float(input()))
    print('Sexo: ')
    validaSexo(input())
    print('Estado Civil: ')
    validaEstadoCivil(input())
    pass
