nome = input('Digite o nome do aluno: ')

valid_nota = False
##Validação da Nota1
while valid_nota == False:
    nota1 = input('Digite a nota da primeira prova: ')
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1> 10:
            print('A nota precisa estar entre 0 e 10')
        else:
            valid_nota = True
    except:
        print("Formato de Nota invalida. Use apenas números e separe os decimais com '.'")

valid_nota = False
##Validação da Nota2       
while valid_nota == False:
    nota2 = input('Digite a nota da segunda prova: ')
    try:
        nota2 = float(nota2)
        if nota2 < 0 or nota2 > 10:
            print('A nota precisa estar entre 0 e 10')
        else:
            valid_nota = True
    except:
        print("Formato de Nota invalida. Use apenas números e separe os decimais com '.'")

valid_faltas = False
##Validação da Falta    
while valid_faltas == False:
    faltas = input('Digite o total de faltas: ')
    try:
        faltas = float(faltas)
        if faltas < 0 or faltas > 20:
            print('As faltas não podem ser menores que 0 e maiores que 20.')
        else:
            valid_faltas = True
    except:
        print("Formato incorreto. utilize apenas números e separe os decimais com '.'")


QtdAulas = 20
PresencaEsperada = QtdAulas*0.3
MediaEsperada = 6
MediaNota = (nota1+nota2)/2
assiduidade = ((QtdAulas-faltas)/QtdAulas)*100

if faltas >= PresencaEsperada and MediaNota < MediaEsperada:
    print('Nome',nome)
    print('Média',MediaNota)
    print('Assiduidade',assiduidade,'%')
    print('Reprovado por faltas e por média')
elif faltas >= PresencaEsperada and MediaNota >= MediaEsperada:
    print('Nome',nome)
    print('Média',MediaNota)
    print('Assiduidade',assiduidade,'%')
    print('Reprovado por faltas')
elif faltas < PresencaEsperada and MediaNota < MediaEsperada:
    print('Nome',nome)
    print('Média',MediaNota)
    print('Assiduidade',assiduidade,'%')
    print('Reprovado por média')
else:
    print('Nome',nome)
    print('Média',MediaNota)
    print('Assiduidade',assiduidade,'%')
    print('APROVADO!!!!')

