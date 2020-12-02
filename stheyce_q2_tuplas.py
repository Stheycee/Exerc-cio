'''
é comum no jogo de dominó ter uma rodada antes de iniciar o jogo na qual todos os integrantes escolhem
apenas uma pedra e quem retirar o maior valor inicia o jogo,
outra situação é quando o jogo fecha e inicia a contagem de pontos, aquele que tiver a menor pontuação vence.
simule um jogo de dominó com quatro jogadore onde deve entrar na tupla os valores para iniciar e outra para
a contagem de pontos no final deve mostrar a maior e menor peça, os valor ordenados.
'''
n = (int(input('Digite o número escolhido para iniciar a partida: ')),
    int(input('Digite o número escolhido: ')), 
    int(input('Digite o número escolhido: ')),  
    int(input('Digite o número escolhido: '))) 
    
print(f'Os números escolhidos foram: {n}')
print('')
print('Os números ordenados: ')
print(sorted(n))
print('')
print('o maior número foi:',max(n))
print('')

b = (int(input('Digite o número escolhido para a contagem de pontos: ')),
    int(input('Digite o número escolhido para a contagem de pontos: ')), 
    int(input('Digite o número escolhido para a contagem de pontos: ')),  
    int(input('Digite o número escolhido para a contagem de pontos: ')))
print(f'Os números escolhidos foram: {b}')
print('')
print('Os números ordenados: ')
print(sorted(b))
print('')
print('o menor número foi:',min(b))



