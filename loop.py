repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    
    while valid_preco == False:
        preco = float(input('Digite o preço do produto: '))
        try:
            preco = float(preco)

            if preco <= 0:
                print('O preço precisa ser maior que 0')
            else:
                valid_preco = True
        except:
            print("Formato de preço invalido. Use apenas números e separe os centavos com '.'")

    fatura.append([produto,preco])
    total += preco
    valid_preco = False

    repetir = input('Deseja informar mais algum produto? s/n ').lower()

for i in fatura:
    print(i[0],'-',i[1])

print('Total da fatura e:',total)
