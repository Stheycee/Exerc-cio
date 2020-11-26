nomes = []
n1 = []
n2 = []
media = []


#quant= int(input('Quantos alunos?'))
print('Insira as notas de 5 alunos')
for C in range (1,6):
    nomes.append(input('Qual é o nome do aluno?'))
    n1.append(input('Qual é a nota 1?'))
    n2.append(input('Qual é a nota 2?'))
    media.append(input('Qual é a media do aluno?'))


print('nº    Nome         média')
print('-------------------------------')
print('0','    ',nomes[0],'  ',media[0])
print('1','    ',nomes[1],'  ',media[1])
print('2','    ',nomes[2],'  ',media[2])
print('3','    ',nomes[3],'  ',media[3])
print('4','    ',nomes[4],'  ',media[4])


resp=int(input('Mostrar as notas de qual aluno?'))

if resp == 0:
    print('Notas de ',nomes[0], 'são ', n101], n2[0])
if resp == 1:
    print('Notas de ',nomes[1], 'são ', n1[1], n2[1])
if resp == 2:
    print('Notas de ',nomes[2], 'são ', n1[2], n2[2])
if resp == 3:
    print('Notas de ',nomes[3], 'são ', n1[3], n2[3])
if resp == 4:
    print('Notas de ',nomes[4], 'são ', n1[4], n2[4])

