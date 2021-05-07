import matplotlib.pyplot as plot
import pdb

fundos = ['ALZR','ARFI','AQLL','BCRI','BNFS','BBFI','BBPO','BBIM','BBRC','RDPD','RNDP','BLMO','BCIA','BZLI','CARE','BRCO','BRIM','BTLG','CRFF','CXRI','CPFF','CPTS','CBOP','GRLV','HGFF','HGLG','HGPO',
'HGRE','HGCR','HGRU','DLMT','DAMT','DOVL','ERPA','KINP','FLCR','VRTA','BMII','BTCR','MTRS','ANCR','FAED','BMLC','BPRP','BRCR','FEXC','BCFF','FCFL','CNES','CEOC','THRA','FAMB','EDGA','ELDO',
'FLRP','HCRI','NSLU','HTMX','MAXR','NCHB','NVHO','PQDP','PATB','PRSV','RBRM','RBRR','JRDM','SHDP','SAIC','TBOF','ALMI','TRNT','RECT','UBSR','VLOL','OUFF','WTSP','VVPR','LVBI','BARI','BBVJ',
'BRHT','BPFF','BVAR','BPML','CXCE','CXTL','CTXT','CJFI','FLMA','EDFO','EURO','GESE','FIGS','ABCP','GTWR','HBTT','HUSC','FIIB','FINF','FMOF','MBRF','MGFF','MVFI','NPAR','OULG','PABY','FPNG',
'ESTQ','VPSI','FPAB','RBRY','RBRP','RCRB','RBED','RBVA','RNGO','SFND','FISC','SCPF','SDIL','SHPH','TGAR','ONEF','TORM','TOUR','FVBI','VERE','FVPQ','FIVN','VTLT','VSHO','IBFF','PLCR','VTPL',
'CVBI','MCCI','ARRI','HOSI','MGHT','IRDM','KFOF','OUCY','GSFI','GGRC','RCFA','HABT','ATCR','HCTR','HAAA','ATSA','HGBS','HLOG','HRDF','HPDP','HMOC','FOFT','HFOF','TFOF','HSML','HUSI','PRGD',
'BICR','RBBV','JPPA','JPPC','JSRE','JTPR','KNHY','KNRE','KNIP','KNRI','KNCR','LATR','LASC','LOFT','LGCP','LUGG','DMAC','MALL','MXRF','MFII','PRTS','SHOP','DRIT','036O','MOFF','NEWL','NVIF',
'FTCE','OUJP','ORPD','PATC','PRSN','PLRI','PORD','PBLV','QAGR','RSPD','RBDS','RBGS','RBCO','FIIP','RBRD','RCRI','RBTS','RBRF','DOMC','RDES','RBIV','RBCB','RBVO','RBFF','SAAG','SADI','SARE',
'FISD','SDIP','WPLZ','REIT','SPTW','SPAF','STRX','SNCR','TSNC','TCPF','XTED','TRXF','V2CR','VGIR','VCJR','VLJS','VIDS','VIFI','VILG','VINO','VISC','VOTS','VXXV','XPCM','XPCI','XPHT','XPIN',
'XPLG','XPML','XPPR','XPSF','YCHY']

meses = []
valores = []
mes = 1
validacao = False
legenda = []
acumulado = 0
mesdescricao = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}

print('Valor calcular a rentabilidade mensal do seu Fundo Imobiliário!')
print('\n')

#Valida se o Fundo existe
while validacao == False:
    ativos = input('Informe a descrição do Fundo Imobiliário: ').upper()
    if fundos.count(ativos) == 1:
        validacao = True
    else:
        print('Fundo imobiliário inválido')

validacao = False

#Valida o valor de compra do Fundo
while validacao == False:
    compra = input('Informe o valor de compra: ')
    try:
        compra = float(compra)
        if compra < 0 :
            print('O valor precisa ser maior que 0')
        else:
            validacao = True
    except:
        print("Valor invalido. Use apenas números e separe os decimais com '.'")

validacao = False

#valida os valores e calcula a rentabilidade mês a Mês    
while mes <= 12:
    while validacao == False:
        valor = input('Digite a cotação do mês de '+mesdescricao.get(mes)+': ')
        try:
            valor = float(valor)
            if valor < 0:
                print('O valor precisa ser maior que 0')
            else:
                validacao = True            
        except:
            print("Valor invalido. Use apenas números e separe os decimais com '.'")

    
    diferenca = valor-compra
    compra += diferenca
    valores.append(diferenca)
    legenda.append(mesdescricao.get(mes))
    meses.append(mes)
    mes += 1
    validacao = False

plot.xticks(meses,legenda)
plot.title('Rentabilidade histórica do '+ativos)
plot.plot(meses,valores)
plot.show()

    
