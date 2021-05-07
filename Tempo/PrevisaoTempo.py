import FuncPrevisaoTempo as func

#Exibe o clime atual pelo IP
try:
    coordenadas = func.pegarCoordenadas()
    func.mostrarPrevisao(coordenadas['lat'],coordenadas['long'])
except:
    print('erro')
#Mostrar previsão do local pesquisado
continuar = 's'

while continuar == 's':
    continuar = input('Deseja consultar a previsão de outro lugar? (s ou n): ').lower()
    if continuar != 's':
        break
    localPesq = input('Digite a cidade: ')
    try:
        coord = func.pegarLocalPesquisado(localPesq)
        func.mostrarPrevisao(coord['lat'],coord['long'])
    except:
        print('erro')
        
        
