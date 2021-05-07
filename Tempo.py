import time as t
import matplotlib.pyplot as plot

tempos = []
tentativas = []
legenda = []
tentativa = 1

print('Este programa marcará o tempo gasto para digitar a palavra "AMOR". Você terá que digita-la 5 vezes')
input('Aperte Enter para começar.')

while tentativa <= 5:
    inicio = t.perf_counter()
    input('Digite a palavra: ')
    fim = t.perf_counter()
    tempo = round(fim - inicio,2)
    tempos.append(tempo)
    tentativas.append(tentativa)
    legenda.append(str(tentativa)+'º vez')
    tentativa += 1

plot.xticks(tentativas,legenda)
plot.plot(tentativas,tempos)
plot.show()
