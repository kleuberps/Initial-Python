cores = {'azul':'blue','vermelho':'red','rosa':'pink','verde':'green'}
cor_sel = input('Digite a cor que deseja traduzir: ').lower()
traducao = cores.get(cor_sel,'Esta cor não consta no meu dicionário')
print(traducao)
