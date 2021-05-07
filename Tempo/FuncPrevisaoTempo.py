import requests
import json
import urllib.parse
from datetime import date


#variaveis
apikey = '5EiossT6ZMUGTJJYxHY0W62qFPpzxPQ0'
mapBoxAPI = 'pk.eyJ1Ijoia2xldWJlcnNlcnJhIiwiYSI6ImNrNHdwb2E2eTRkbDkza25zNnNrYnFpdm8ifQ.TXVe8hoTaCZynyYLFN-xPA'
diaSemana = ['Domingo','Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sabado']


def pegarCoordenadas():
    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code != 200):
        print('Não foi possivel obter a localização')
        return None
    else:
        try:
            localizacao = json.loads(r.text)
            coordenadas = {}
            coordenadas['lat'] = localizacao['geoplugin_latitude']
            coordenadas['long'] = localizacao['geoplugin_longitude']
            return coordenadas
        except:
            return None

def pegarCodigoLocal(lat,long):    

    apiurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
             + "search?apikey=" + apikey \
             + "&q=" + lat + "%2C" + long + "&language=pt-br"
    
    r = requests.get(apiurl)
    if (r.status_code != 200):
        print('Não foi possivel obter o código do local')
        return None
    else:
        try:
            locationresponse = json.loads(r.text)
            infoLocal = {}
            infoLocal['nomeLocal'] = locationresponse['LocalizedName']+', '\
                        + locationresponse['AdministrativeArea']['LocalizedName']+' - '\
                        + locationresponse['Country']['LocalizedName']
            infoLocal['codigoLocal'] = locationresponse['Key']
            return infoLocal        
        except:
            return None

def pegarPrevisao(codigoLocal):
    
    previsaoAPI = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" \
                  + codigoLocal + "?apikey=" + apikey + "&language=pt-br&metric=true"

    r = requests.get(previsaoAPI)
    if (r.status_code != 200):
        print('Não foi possivel obter o código do local')
        return None
    else:
        try:
            t = json.loads(r.text)
            infoClima5Dias = []
            for dia in t['DailyForecasts']:
                climaDia = {}
                climaDia['max'] = dia['Temperature']['Maximum']['Value']
                climaDia['min'] = dia['Temperature']['Minimum']['Value']
                climaDia['clima'] = dia['Day']['IconPhrase']
                DiaSemana = int(date.fromtimestamp(dia['EpochDate']).strftime("%w"))
                climaDia['dia'] = diaSemana[DiaSemana]
                infoClima5Dias.append(climaDia)
            return infoClima5Dias
        except:
            return None

def mostrarPrevisao(lat, long):
    try:
        local = pegarCodigoLocal(lat,long)
        climaAtual = pegarTempoAgora(local['codigoLocal'],local['nomeLocal'])
        print('Clima atual em: '+climaAtual['nomeLocal'])
        print(climaAtual['textoClima'])
        print('Temperatura: '+str(climaAtual['temperatura'])+'°C')
    except:
        print('Erro ao obter o clima atual.')

    climaProximosDias = input('\nExibir o clima para os próximos 5 dias? (s ou n): ').lower()
    try:
        #Clima para os proximos dias
        if climaProximosDias == 's':
            print('\nClima para hoje e para os próximos dias:\n')
            previsao5Dias = pegarPrevisao(local['codigoLocal'])
            for dia in previsao5Dias:
                print(dia['dia'])
                print('Mínima: '+ str(dia['min'])+'°C')
                print('Máxima: '+ str(dia['max'])+'°C')
                print('Clima: '+ dia['clima'])
                print('-----------------------------------------------------')
    except:
        print('Erro ao obter o clima dos proximos 5 dias.')
    
def pegarLocalPesquisado(local):
    
    _local = urllib.parse.quote(local)
    
    APIpesquisa = "https://api.mapbox.com/geocoding/v5/mapbox.places/" \
                  + _local + ".json?access_token=" + mapBoxAPI

    r = requests.get(APIpesquisa)
    if (r.status_code != 200):
        print('Não foi possivel obter o local pesquisado')
        return None
    else:
        try:
            t = json.loads(r.text)
            for coordenadas in t['features'][0]:
                coordenada = {}
                coordenada['lat'] = str(t['features'][0]['center'][1])
                coordenada['long'] = str(t['features'][0]['center'][0])
            return coordenada
        except:
            return None

def pegarTempoAgora(codigoLocal, nomeLocal):
    
    ClimaApi = "http://dataservice.accuweather.com/currentconditions/v1/"+codigoLocal+"?" \
               + "apikey="+apikey+"&language=pt-br"


    r = requests.get(ClimaApi)
    if (r.status_code != 200):
        print('Não foi possivel obter o clima atual')
        return None
    else:
        try:
            Condicaoclima = json.loads(r.text)
            infoClima = {}
            infoClima['textoClima'] = Condicaoclima[0]['WeatherText']
            infoClima['temperatura'] = Condicaoclima[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        except:
            return None
