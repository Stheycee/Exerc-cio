'''
Na rede SESI, alunos com pai ou mãe fincionário da industria possuem o direito de receber descontos na mensalidade,
digamos que o desconto seja de 10%, faça um programa que simule a matricula de um aluno, onde:
1- insira o nome, ano de nascimento
2- pergunte ao usuario se tem ou não pais fincionários da industria
    -caso não: mostrar nome, ano de nascimento, idade e quando iria terminar o ensino médio.
    -caso sim: continuar as perguntas tais como
        -Número da matricula de funcionário da industria
        -o salário
        -calcular o desconto de 10% na mensalidade com valor de 450 reais
        - mostrar mostrar nome, ano de nascimento, idade e quando iria terminar o ensino médio.
        - mostrar o valor do desconto e quanto vai ficar a mensalidade
'''
dici = {}
from datetime import datetime
ano = datetime.now().year
dici['nome'] = str(input('NOME: '))
dici['nasc'] = int(input('NASCIMENTO: '))
idade = datetime.now().year - dici['nasc']
termino = ano + 3
dici['industria'] = str(input('Filho de funcionario da industria? S/N  '))
if dici['industria'] in 'Nn':
    print(f'{dici["nome"]}, que nasceu em {dici["nasc"]}, com idade de {idade} anos, está matriculado na rede SESi de ensino, previsto para terminar os estudos no ano de {termino}') 
if dici['industria'] in 'Ss':
   dici['matricula'] = int(input('Número da matricula de funcionário da industria: '))
   dici['salario'] = float(input('SALÁRIO: R$ '))
   dici['desconto'] = dici['salario']*10/100
   dici['mensalidade'] = 450 - dici['desconto']
   print(dici)

for k, v in dici.items():
    print(f'{k} = {v}')
print()
print(f'{dici["nome"]}, que nasceu em {dici["nasc"]}, com idade de {idade} anos, está matriculado na rede SESi de ensino, previsto para terminar os estudos no ano de {termino}')
print(f'{dici["nome"]}, com familiar funcionário na industria teve direito ao desconto de {dici["desconto"]} reais, passando a ter a mensalidade no valor de {dici["mensalidade"]}')