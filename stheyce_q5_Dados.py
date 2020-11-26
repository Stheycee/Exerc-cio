from random import randint
from operator import itemgetter
jogos = {}
print('Valores sorteados:')
for j in range(1, 5):
    jogos[f'jogador{j}'] = randint(1, 6)
for k, v in jogos.items():
    print(f'   O {k} tirou {v}')
podio = sorted(jogos.items(), key=itemgetter(1), reverse=True)
jogos.clear()
for j in range(0, 4):
    jogos[f'{podio[j][0]}'] = podio[j][1]
print('Ranking dos Jogadores:')
pos = 1
for k, v in jogos.items():
    print(f'   {pos}º lugar: {k} com {v}')
    pos += 1