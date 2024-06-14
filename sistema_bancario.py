
print("\n\n")
print(" Seja muito bem-vindo ao MyUser Bank! ".center(50, "-"))

menu = """

    =============== MENU ===============

            O que deseja operar?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        print("\n")
        print("=> Depósito".center(30))
        print("\n")
        valor = float(input("Quanto gostaria de depositar? Coloque o valor com '.' se precisar definir a quantidade de centavos.\n R$ "))
        
        while valor < 0:
            print("Valor inválido! Digite novamente o valor a ser depositado ou digite 0 para voltar nas opções: ")
            valor = float(input("R$ "))

            if valor == 0:
                print("Depósito cancelado.")
                continue
            
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"R${valor:.2f} foi depositado.")
        print("\n")


    elif opcao == "s":
        print("\n")
        print("=> Saque".center(30))
        print("\n")
        print(f"Seu saldo disponível: R$ {saldo:.2f}")
        
        valor = float(input("Quanto gostaria de sacar? Coloque o valor com '.' se precisar definir a quantidade de centavos.\nR$ "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if not excedeu_saques:
                
            if valor == 0:
                print("Saque cancelado.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
                valor = 0

            elif excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
                
            elif valor < 0:
                print("Valor não existente para saque!")
        
            if valor <= saldo and valor > 0:
                print(f"Valor sacado: R$ {valor:.2f}")
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}.\n"
                numero_saques += 1

        else:
            print("Quantidade de saques diários excedido! Tente novamente amanhã ou fale com o seu gerente!")
        print("\n")


    elif opcao == "e":
        print("\n")
        print(" Extrato ".center(50, "="))
        print("\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo : R$ {saldo:.2f}\n")
        print("".center(50, "="))

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
    print("\n")


print("Obrigado por usar o nosso sistema!")
print(" Volte sempre!!! ".center(30, "-"))
print("\n\n")