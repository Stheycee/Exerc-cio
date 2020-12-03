
def maior(*num):
    if len(num) > 0:
        print(f'O maior de {num} é o {max(num)}.')
        print(f'O menor de {num} é o {min(num)}.')
        print('')
    
maior(15, 1, 11, 66, 3)
maior(14, 7, 10, 2)
maior(1, 2, 3, 7, 3, 9, 5, 12)
maior(1)
maior(1, 2)
maior(44,28,15,17)
