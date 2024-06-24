
import textwrap

print("\n\n")
print(" Seja muito bem-vindo ao MyUser Bank! ".center(50, "-"))

def menu():
    menu = """\n
    =============== MENU ===============

            O que deseja operar?

    [d]\tDepositar  
    [e]\tExtrato
    [s]\tSacar
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário        
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    
    while valor < 0:
        print("\n@@@ Valor inválido! Digite novamente o valor a ser depositado ou digite 0 para voltar nas opções: ")
        valor = float(input("R$ "))

        if valor == 0:
            print("Depósito cancelado.")
            continue
        
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
        print(f"R${valor:.2f} foi depositado.\n")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if not excedeu_saques:
            
        if valor == 0:
            print("Saque cancelado.")

        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite.")
            valor = 0

        elif excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente.")
            
        elif valor < 0:
            print("\n@@@ Valor não existente para saque!")
    
        if valor <= saldo and valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
            print(f"Valor sacado: R$ {valor:.2f}")
    else:
        print("\n@@@ Quantidade de saques diários excedido! Tente novamente amanhã ou fale com o seu gerente!")
        print("\n")        
    
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n")
    print(" Extrato ".center(50, "="))
    print("\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo : \tR$ {saldo:.2f}\n")
    print("".center(50, "="))

    return saldo, extrato


def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário criado com sucesso! ===".center(50, " "))


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(AGENCIA, numero_conta, usuarios): 
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===".center(50, " "))
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "d":
            print("\n")
            print("=> Depósito".center(30))
            print("\n")
            valor = float(input("Quanto gostaria de depositar? Coloque o valor com '.' se precisar definir a quantidade de centavos.\n R$ "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            print("\n")
            print("=> Saque".center(30))
            print("\n")
            print(f"Seu saldo disponível: R$ {saldo:.2f}")

            valor = float(input("Quanto gostaria de sacar? Coloque o valor com '.' se precisar definir a quantidade de centavos.\nR$ "))

            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida! Por favor, selecione novamente a operação desejada.")
            print("\n")

main()

print("\n\nObrigado por usar o nosso sistema!")
print(" Volte sempre!!! ".center(30, "-"))
print("\n\n")


