from random import choice
from time import sleep
def veri(a):
    if ppt == '1' or ppt == '2' or ppt == '3':
        if ppt == '1':
             print(f'{nome}: Pedra')
        elif ppt == '2':
             print(f'{nome}: Papel')
        elif ppt == '3':
              print(f'{nome}: Tesoura')
        sleep(0.75)


def cação(b):
        if comp == 1:
            print(f'Computador: Pedra')
        elif comp == 2:
            print(f'Computador: Papel')
        elif comp == 3:
            print(f'Computador: Tesoura')
        sleep(0.75)


print('''Bem vindo ao JokenPy.
intruções:
'1' para Pedra
'2' para Papel
'3' para Tesoura''')
nome = input('Login: ')
print('=' * 80)


ppt = input('Pedra, Papel, Tesoura...').strip()
veri(ppt)
comp = choice([1, 2, 3])
cação(comp)
if ppt == str(comp):
    print('Computador: Ops, empatamos!')
elif (ppt == '1' and comp == 2)or (ppt == '2' and comp == 3)or (ppt == '3' and comp == 1):
    print('Computador: Há ! Eu ganhei !')
else:
    print('Computador: Parabéns ! Você venceu.')

 
    