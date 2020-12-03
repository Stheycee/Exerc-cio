'''
Com o passar do tempo os signos ganharam bastante popularidade, vindo de encontro também temos os Zodíaco Chinês
levando em conta que não é muito visto no nosso cotidiano, faça um programa que ajude as pessoas a descobrirem
seu signo do Zodíaco Chinês.
Levando em cosideração que ele é composto por animais com ciclo de 12 anos uma maneira simples de identificar é 
com o ano do nascimento.
ano do nascimento % 12, sendo
0- macaco
1-galo
2-Cão
3-Porco
4-Rato
5-Boi
6- Tigre
7-coelho
8-Dragão
9-Serpente
10-Cavalo
11-Carneiro
'''

ano = int(input('Digite seu ano de nascimento: '))
signos = ['Macaco','Galo','Cão','Porco','Rato','Boi','Tigre','coelho',
'Dragão','Serpente','Cavalo','Carneiro']
signos = signos[ano%12]
print(f'O seu signo do Zodíaco Chinês é {signos}.')
