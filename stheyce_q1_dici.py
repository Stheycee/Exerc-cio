'''
Em faculdades é normal os alunos trabalharem para a instituição para ganhar descontos na mensalidade e seu salário.
é comum esses estudantes tratalharem divulgando a instituição e procurando pessoas para efetuarem matriculas e 
participarem de vestibulares para entrar nos cursos que escolheram.
Normalmente o cadastro inicial é feito com caneta e papel, já que é mais facil, rapido e mais seguro quando
se trabalha na rua. Levando em consideração isso, faça um programa que simule a entrada desses dados:
nome,idade, sexo.
o programa deve rodar até o usuario não querer mais. 
- é necessária a validação caso o sexo seja digitado errado. 
-mostrar quantas pessoas cadastradas, a média das idades, quem está acima dessa média. 
'''
pessoas=[]
media=0
cont=0
while True:
    pessoas.append({"nome":input("Nome:").title().strip()})
    pessoas[cont]["sexo"]=input("Sexo [F/M]:").upper().strip()
    while pessoas[cont]["sexo"] not in "FM":
        print("ERRO! Por favor, digite apenas M ou F.")
        pessoas[cont]["sexo"]=input("Sexo [F/M]:").upper().strip()
    pessoas[cont]["idade"]=int(input("Idade:"))
    media+=pessoas[cont]["idade"]
    cont+=1
    r=input("Quer continuar?[S/N]:").strip()
    while r not in "snSN":
        print("ERRO! Responda apenas S ou N.")
        r=input("Quer continuar?[S/N]:").strip()
    if r == "n":
        break
media/=len(pessoas)
print("=-"*35)
print(f" Foram cadastradas {len(pessoas)} pessoas.")
print(pessoas)
print(f" A média de idade é de {media} anos.")
print()
print(" Lista de pessoas com a idade acima da média:")
for c in pessoas:
    if c["idade"]>media:
        for k,v in c.items():
            print(f"{k:>8} = {v:<14}",end="")
        print()
