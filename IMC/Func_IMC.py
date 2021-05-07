def CalcIMC(peso,altura):
    Resultado = round(peso/(altura*altura),2)
    return Resultado

def ClassificacaoIMC(peso,altura,sexo):
    
    resultIMC = CalcIMC(peso,altura)
    
    if sexo == 'f':
        if resultIMC < 19.1:
            return 'você está abaixo do peso'
        elif resultIMC >= 19.1 and resultIMC < 25.8:
            return 'Parabéns, você está no peso normal'
        elif resultIMC >= 25.8 and resultIMC < 27.3:
            return 'você está marginalmente acima do peso'
        elif resultIMC >= 27.3 and resultIMC < 32.3:
            return 'você está acima do peso ideal'
        elif resultIMC >= 32.3:
            return 'você está obeso'
    elif sexo == 'm':
        if resultIMC < 20.7:
            return 'você está abaixo do peso'
        elif resultIMC >= 20.7 and resultIMC < 26.4:
            return 'Parabéns, você está no peso normal'
        elif resultIMC >= 26.4 and resultIMC < 27.8:
            return 'você está marginalmente acima do peso'
        elif resultIMC >= 27.8 and resultIMC < 31.1:
            return 'você está acima do peso ideal'
        elif resultIMC >= 31.1:
            return 'você está obeso'

