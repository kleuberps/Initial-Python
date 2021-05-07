meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
data_nasc = input('Digite sua data de nascimento no formado DD/MM/AAAA: ')
mes_nascimento = int(data_nasc[3:5])-1
print('Você nasceu no mês de:',meses[mes_nascimento])
