def gorjeta(conta):
    b= conta*10/100
    return conta+b

    

r=str(input('Desaja pagar a gorjeta? S/N '))
if r in 'Ss':
    a = float(input('Qual é o valor da conta?'))
    print(f'Valor total da conta: {gorjeta(a)}')
else:
    c = float(input('Qual é o valor da conta?'))
    print(f'Valor total da conta: {c}')