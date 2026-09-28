print("==========================================")
print("       PESQUISA DE OPINIÃO - TUDOWEB")
print("==========================================")

excelente = 0
ruim = 0

for i in range(1, 51):

    print("\n------------------------------------------")
    print("ENTREVISTADO", i)

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\n==========================================")
print("          RESULTADO DA PESQUISA")
print("==========================================")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
print("==========================================")