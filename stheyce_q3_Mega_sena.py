from random import randint
listadebolas = [] 
jogo=int(input('Quantos sorteios deseja?'))

for C in range(jogo):
    bola1 = randint(1,60)
    bola2 = randint(1,60)
    bola3 = randint(1,60)
    bola4 = randint(1,60)
    bola5 = randint(1,60)
    bola6 = randint(1,60)

# Sorteio da Bola 2 novamente se for repetida
    while bola2 == bola1:
         bola2 = randint(1,60)

# Sorteio da Bola 3 novamente se for repetida
    while bola3 == bola2 or bola3 == bola1:
        bola3 = randint(1,60)

# Sorteio da Bola 4 novamente se for repetida
    while bola4 == bola3 or bola4 == bola2 or bola4 == bola1:
        bola4 = randint(1,60)

# Sorteio da Bola 5 novamente se for repetida
    while bola5 == bola4 or bola5 == bola3 or bola5 == bola2 or bola5 == bola1:
         bola5 = randint(1,60)

# Sorteio da Bola 6 novamente se for repetida
    while bola6 == bola5 or bola6 == bola4 or bola6 == bola3 or bola6 == bola2 or bola6 == bola1:
        bola6 = randint(1,60)

# Inclusão das bolas na lista
    listadebolas.append(bola1)
    listadebolas.append(bola2)
    listadebolas.append(bola3)
    listadebolas.append(bola4)
    listadebolas.append(bola5)
    listadebolas.append(bola6)


    print(bola1,bola2,bola3,bola4,bola5,bola6)
    #print(sorted(listadebolas))

