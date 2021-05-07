import Func_IMC

print('Vamos calcular seu IMC?')

validacao = False
## Validação Peso
while validacao == False:
    peso = input('Digite seu peso: ')
    try:
        peso = float(peso)
        if peso <= 0 or peso >= 300:
            print('Peso invalido. O numero não pode ser 0 ou negativo e deve ser inferior a 300.')
        else:
            validacao = True
            print('\n')
    except:
        print('Peso invalido. Utilize apenas números e separe os decimais com ponto.')

#validacao Altura
validacao = False
while validacao == False:
    altura = input('Digite sua altura em metros (ex: 1.70): ')
    try:
        altura = float(altura)
        if altura <= 0 or altura >= 3:
            print('Peso invalido. O numero não pode ser 0 ou negativo e deve ser inferior a 3 metros')
        else:
            validacao = True
            print('\n')
    except:
        print('Altura invalido. Utilize apenas números e separe os decimais com ponto.')        

#validacao Sexo
validacao = False
while validacao == False:
    sexo = input('Digite seu sexo (M ou F): ').lower()
    if sexo != 'f' and sexo != 'm':
        print('Sexo invalido. Digite apenas M ou F')
    else:
        validacao = True
        print('\n')

v_IMC = Func_IMC.CalcIMC(peso,altura)
v_classificacao = Func_IMC.ClassificacaoIMC(peso,altura,sexo)

print('\nRESULTADO')
print('\nSeu IMC é de:',v_IMC)
print(v_classificacao)
