'''
Joana deseja fazer uma festa, para isso ela quer fazer uma lista com todos os seus amigos como convidados,
mas joana tem muitos e muitos amigos e se perdeu quando colocou os nomes e já não sabe qual nome adicionou. 
Faça um programa que ajude joana a listar todos os seus amigos, caso já tenha um nome na lista mostrar uma
mensagem para avisar que o nome já existe. No final mostrar a lista completa e quantos convidados joana listou. 
'''
nome=[]
while True:
    n=str(input('Qual é o nome que você deseja adicionar?'))
    if n not in nome:
        nome.append(n)
        print('Nome adicionado na lista')
        print('')
    else:
        print('Nome já existe na lista')
    r=str(input('Quer continuar? S/N    '))
    print('')
    if r in 'Nn':
        print('')
        print(f'Lista com {len(nome)} convidados')
        print('A lista foi finalizada,Todos os convidados são:')
        print(nome)
        break

