import random

def tem_barco(tab):
    for line in tab:
        if '░░ ' in line:
            return True
    return False


print('\u2693')
n = int(input("Digite  a quantidade de casas por EX 10x10"))
x = 1
ne = [['██  ']*n]*n
##for line in ne:
##    print("".join(line) + (" "))
def tabu(ne):
   
    print('   ' + '  '.join([str(i).center(2) for i in range(len(ne))]))
    for i in range(len(ne)):
        print('%2d %s' % (i + 0, ''.join(ne[i])))
        print()

def tabum1(matriz):
    for line in matriz:
        print(" ".join(line) + ("   "))
        print()

def tabum2(matriz2):
    for line in matriz2:
        print(" ".join(line) + ("   "))
        print()
##for line in ne:
##    print("".join(line) + (" "))
tabu(ne)
print()
print()
print()
##for line in ne:
##    print("".join(line) + (" "))
lista = []
linha = []
nc = 1
nl = n
for c in range(0, nl):
    lista.append([])
for c1 in range(0, nl):
    for c2 in range(0, nl):
        lista[c1].append('██ ')
matriz = lista
##for c1 in range(0, nl):
##    print(matriz[c1])
##---------------------------------------------##
lista2 = []
linha2 = []
nc2 = 1
nl2 = n
for c in range(0, nl2):
    lista2.append([])
for c1 in range(0, nl2):
    for c2 in range(0, nl2):
        lista2[c1].append('██ ')
matriz2 = lista2


def nav1(matriz):
    print(tabu(ne))


## ------------------------------------------------------------------------destribuição--dos--naios----------------------------------------------------------------------

print('porta_aviões(comprimento 5) ░░░░░░░░░░')
print('encouraçado (comprimento 4) ░░░░░░░░')
print('submarino (comprimento 3) ░░░░░░')
print('destroyer(comprimento 3) ░░░░░░')
print('barco (comprimento 2) ░░░░')
porta_aviões = 5
encouraçado = 4
submarino = 3
destroyer = 3
barco = 2




##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


j1 = str(input('digite seu nome jogador 1 :'))
j2 = str(input('digite seu nome jogador 2 :'))
print('Ola , voce devera posicionar os seus barcos !!')
x = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
print('digite a linha e a coluna para posicionar o barco = 2 casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x < barco):

    if dire == 'l':
        matriz[linha][coluna] = '░░ '
        matriz[linha][coluna + x] = '░░ '
    elif dire == 'n':
        matriz[linha][coluna] =  '░░ '
        matriz[linha - x][coluna] = '░░ '
    elif dire == 's':
        matriz[linha][coluna] = '░░ '
        matriz[linha + x][coluna] = '░░ '
    elif dire == 'o':
        matriz[linha][coluna] = '░░ '
        matriz[linha][coluna - x] = '░░ '

    x = x  + 1
tabum1(matriz)

##----------------------------------------------------------------------------------------------------------##      
print('digite a linha e a coluna para posicionar o destroyer = 3  casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x1 < destroyer):
   
    if dire == 'l':
        matriz[linha][coluna + x1] = '░░ '

    elif dire == 'n':
        matriz[linha - x1][coluna] = '░░ '

    elif dire == 's':
        matriz[linha + x1][coluna] = '░░ '
    elif dire == 'o':
        matriz[linha][coluna - x1] = '░░ '
 
    x1 = x1 + 1

   
tabum1(matriz)
##----------------------------------------------------------------------------------------------------------##  


print('digite a linha e a coluna para posicionar o submarino = 6 casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x2 < submarino):
    if dire == 'l':
        matriz[linha][coluna + x2] = '░░ '
               
    elif dire == 'n':
        matriz[linha - x2][coluna] = '░░ '

    elif dire == 's':

        matriz[linha + x2][coluna] = '░░ '
    elif dire == 'o':

        matriz[linha][coluna - x2] = '░░ '
    x2 = x2 + 1
tabum1(matriz)
##----------------------------------------------------------------------------------------------------------##  

print('digite a linha e a coluna para posicionar o encouraçado = 4 casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x3 <= encouraçado):    

    if dire == 'l':

        matriz[linha][coluna + x3] = '░░ '
       
    elif dire == 'n':

        matriz[linha - x3][coluna] = '░░ '

    elif dire == 's':


        matriz[linha + x3][coluna] = '░░ '
    elif dire == 'o':

        matriz[linha][coluna - x3] = '░░ '
   
    x3 = x3 + 1
tabum1(matriz)
##----------------------------------------------------------------------------------------------------------##  
print('digite a linha e a coluna para posicionar o porta_aviões = 5 casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x4 <= porta_aviões):

    if dire == 'l':

        matriz[linha][coluna + x4] = '░░ '
       
    elif dire == 'n':

        matriz[linha - x4][coluna] = '░░ '

    elif dire == 's':

        matriz[linha + x4][coluna] = '░░ '
    elif dire == 'o':
        matriz[linha][coluna - x4] = '░░ '
    x4 = x4 + 1
tabum1(matriz)







    
##----------------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------##

tabu(ne)

##------------------------------------------------------------------------------------------------
##------------------------------------------------------------------------------------------------
##------------------------------------------------------------------------------------------------

print('Agora e sua vez %s de posicionar os barco !!' % j2)
print('Ola , voce devera posicionar os seus barcos !!')
x = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
print('digite a linha e a coluna para posicionar o barco = 2 casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x < barco):

    if dire == 'l':
        matriz2[linha][coluna] = '░░ '
        matriz2[linha][coluna + x] = '░░ '
    elif dire == 'n':
        matriz2[linha][coluna] = '░░ '
        matriz2[linha - x][coluna] = '░░ '
    elif dire == 's':
        matriz2[linha][coluna] = '░░ '
        matriz2[linha + x][coluna] = '░░ '
    elif dire == 'o':
        matriz2[linha][coluna] = '░░ '
        matriz2[linha][coluna - x] = '░░ '

    x = x  + 1

tabum2(matriz2)
##----------------------------------------------------------------------------------------------------------##      
print('digite a linha e a coluna para posicionar o destroyer = 3  casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x1 < destroyer):
   
    if dire == 'l':
        matriz2[linha][coluna + x1] = '░░ '

    elif dire == 'n':
        matriz2[linha - x1][coluna] = '░░ '

    elif dire == 's':
        matriz2[linha + x1][coluna] = '░░ '
    elif dire == 'o':
        matriz2[linha][coluna - x1] = '░░ '
 
    x1 = x1 + 1

tabum2(matriz2)
   

##----------------------------------------------------------------------------------------------------------##  


print('digite a linha e a coluna para posicionar o submarino = 6 casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x2 < submarino):
    if dire == 'l':
        matriz2[linha][coluna + x2] = '░░ '
               
    elif dire == 'n':
        matriz2[linha - x2][coluna] = '░░ '

    elif dire == 's':

        matriz2[linha + x2][coluna] = '░░ '
    elif dire == 'o':

        matriz2[linha][coluna - x2] = '░░ '
    x2 = x2 + 1

tabum2(matriz2)

##----------------------------------------------------------------------------------------------------------##  

print('digite a linha e a coluna para posicionar o encouraçado = 4 casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x3 <= encouraçado):    

    if dire == 'l':

        matriz2[linha][coluna + x3] = '░░ '
       
    elif dire == 'n':

        matriz2[linha - x3][coluna] = '░░ '

    elif dire == 's':


        matriz2[linha + x3][coluna] = '░░ '
    elif dire == 'o':

        matriz2[linha][coluna - x3] = '░░ '
   
    x3 = x3 + 1

tabum2(matriz2)


##----------------------------------------------------------------------------------------------------------##  
print('digite a linha e a coluna para posicionar o porta_aviões = 5 casas')
linha = int(input('digite a linha'))
coluna = int(input('digite a coluna'))
dire = str(input('digite para que direcao n = norte s = sul o = oeste l = leste'))
while (x4 <= porta_aviões):

    if dire == 'l':

        matriz2[linha][coluna + x4] = '░░ '
       
    elif dire == 'n':

        matriz2[linha - x4][coluna] = '░░ '

    elif dire == 's':

        matriz2[linha + x4][coluna] = '░░ '
    elif dire == 'o':
        matriz2[linha][coluna - x4] = '░░ '
    x4 = x4 + 1


tabum2(matriz2)

##----------------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------##


print("Agora vocês iram lançar suas bombas até acabar as embarcações !!!")
print("lembrando que vocês devem asertar todas as casas que uma embarcaçõa possui !!!")
print("vocês iram comesar lançar suas bombas boa sorte !!!")
print('Você devera lançar suas bombas em lugares validos que não fuja do campo de batalha')
print('Digite a linha e a coluna que você quer que a bomba atingir lembrando que quando você atigir um naviua bomba destruira uma casa do naviu !!')
xd = False

while xd == False:
    print(j1, 'é sua vez')
    tabu(ne)
    bombalinha1 = int(input('Digite a linha --->'))
    bombacoluna1 = int(input('Digite a coluna --->'))
    if matriz2[bombalinha1][bombacoluna1] == '██':
        print("Você errou TCHÊ!")
    if matriz2[bombalinha1][bombacoluna1] == '░░':
        matriz2[bombalinha1][bombacoluna1] = '██'
        print('　　　　　＼　　　　　　☆')
        print('　　　　　　　　　　　　　|　　　　　☆')
        print('　　　　　　　　　　(⌒ ⌒ヽ　　　/')
        print('　　　　＼　　（´⌒　　⌒　　⌒ヾ　　　／')
        print('　　　　　 （’⌒　;　⌒　　　::⌒　　）')
        print('　　　　　（´　　　　　）　　　　　:::　）　／')
        print('　　☆─　（´⌒;:　　　　::⌒`）　:;　　）')
        print('　　　　　（⌒::　　　::　　　　　::⌒　）')
        print('　　 　／　（　　　　ゝ　　ヾ　丶　　　─')
        print('-------------------------------------------')


        print('     PARABENS VOCÊ ACERTOU UM BARCO TCHÊ !!!')

        print('mas ba tchê tu levo chumbo', j2)
   
    ##--------------------------------------------------------##
    if not tem_barco(matriz2):
        print(j1, 'PARABENS VOCÊ VENCEU')


    ##--------------------------------------------------------##  

    print(j2, 'é sua vez')
    tabu(ne)
    bombalinha2 = int(input('Digite a linha --->'))
    bombacoluna2 = int(input('Digite a coluna --->'))
    if matriz2[bombalinha2][bombacoluna2] == '██':
        print("Você errou THÊ!")
    if matriz2[bombalinha1][bombacoluna1] == '░░':
        matriz2[bombalinha1][bombacoluna1] = '██'
        print('　　　　　＼　　　　　　☆')
        print('　　　　　　　　　　　　　|　　　　　☆')
        print('　　　　　　　　　　(⌒ ⌒ヽ　　　/')
        print('　　　　＼　　（´⌒　　⌒　　⌒ヾ　　　／')
        print('　　　　　 （’⌒　;　⌒　　　::⌒　　）')
        print('　　　　　（´　　　　　）　　　　　:::　）　／')
        print('　　☆─　（´⌒;:　　　　::⌒`）　:;　　）')
        print('　　　　　（⌒::　　　::　　　　　::⌒　）')
        print('　　 　／　（　　　　ゝ　　ヾ　丶　　　─')
        print('-------------------------------------------')


        print('     PARABENS VOCÊ ACERTOU UM BARCO TCHÊ !!!')

        print('mas ba tchê tu levo chumbo', j1)


        if not tem_barco(matriz):
            print(j2, 'PARABENS VOCÊ VENCEU')
