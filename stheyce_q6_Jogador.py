jogador = dict()
goll = list()
jogador['name'] = str(input('Nome do jogador: '))
par = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(par):
    goll.append(int(input(f'Quantos gols ele fez na partida {i}? ')))
    jogador['gols'] = goll
    jogador['total'] = sum(goll)
print('-=-' * 12)
print(jogador)
print('-=-' * 12)
for k, v in jogador.items():
    print(f'O campo "{k}" vale: {v}')
print('-=-' * 12)
print(f'O jogador {jogador["name"]} jogou {par} partidas')
for i, g in enumerate(goll):
    print(f'    -> Na partida {i}, fez {g} gols')
print(f'Foi um total de {jogador["total"]}')