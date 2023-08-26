import textwrap
def menu():
    menu = f"""
    =============== MENU ================
    Escolha a operação desejada:
    [DE] Depositar
    [SA] Sacar
    [EX] Extrato
    [NC] Nova conta
    [LC] Listar contas
    [NU] Novo usuário
    [Q]  Sair
     ======================================
    => """
    return input (menu)
def deposito(saldo, extrato, valor_deposito,/):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
        print("Deposito realizado com sucesso!")

    else:
        print("Operação falhou! O valor inserido é inválido!")

    return saldo, extrato
def saques(*,saldo, extrato, valor_saque, limite, numero_saques ,LIMITE_SAQUES):

    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_limite:
        print("Operação falhou! O valo máximo por saque é de R$500,00!")

    elif excedeu_saldo:
        print("Operação falhou! O valor do saque é maior que o saldo disponivel!")


    elif excedeu_saques:
        print("Operação falhou! O limite diário de saques foi atingido!")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor inserido é inválido!")

    return saldo, extrato, numero_saques
def extratos (saldo,/, extrato):
    print(("=" * 15) + ("Extrato") + ("=" * 15))
    print("Não foram realizados movimentações" if not extrato else extrato)
    print(f'\n Saldo R$ {saldo:.2f}')
    print(f'=' * 37)
def novo_usuario (usuarios):

    while True:
        try:
            cpf = str(input("Informe o seu CPF:"))
            if len(cpf) == 11:
                break
            else:
                print("O valor digitado é inválido! Tente novamente!")
        except ValueError:
            print("Operação inválida! Entre com um valor válido!")

    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário cadastrado com esse CPF!")
        return

    nome = input("Entre com seu nome completo:")
    data_nascimento = input("Entre com sua data de nascimento(dd-mm-aaaa):")
    endereço = input("Informe o endereço (logradouro, número, bairro - cidade/sigla estado):")

    usuarios.append ({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereço": endereço})
    return cpf
def filtra_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None
def criar_conta(agencia, numero_conta, usuarios,contas):
    while True:
        try:
            cpf = str(input("Informe o seu CPF:"))
            if len(cpf) == 11:
                break
            else:
                print("O valor digitado é inválido! Tente novamente!")
        except ValueError:
            print("Operação inválida! Entre com um valor válido!")

    usuario = filtra_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    else:
        print("Usuário não encontrado!")
def listar_contas (contas):
    if len(contas) != 0:
        for conta in contas:
            listar = f"""
                Agência:{conta['agencia']}
                Nº conta:{conta['numero_conta']}
                Titular:{conta['usuario']['nome']}
            """
            print("="*50)
            print(textwrap.dedent(listar))

    else:
        print(textwrap.dedent("Não existe contas criadas!"))
def main ():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu().casefold()
        try:
            if opcao == "de":
                valor_deposito = float(input("Escolha o valor a ser depositado:"))
                saldo, extrato = deposito(saldo,extrato, valor_deposito)

            elif opcao == "sa":
                valor_saque = float(input("Escolha o valor a ser sacado:"))
                saldo, extrato, numero_saques = saques(saldo = saldo, extrato = extrato , valor_saque = valor_saque, limite = limite, numero_saques = numero_saques,LIMITE_SAQUES = LIMITE_SAQUES)

            elif opcao == "ex":
                extratos (saldo, extrato = extrato)

            elif opcao == "nu":
                novo_usuario(usuarios)

            elif opcao == "nc":
                numero_conta = len(contas) + 1
                criar_conta(AGENCIA,numero_conta,usuarios,contas)

            elif opcao == "lc":
                listar_contas(contas)

            elif opcao == "q":
                break

            else:
                print("Operação inválida! Entre com um valor válido!")

        except ValueError:
            print("Operação inválida! Entre com um valor válido!")

main()
