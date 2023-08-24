menu = """
Escolha a operação desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = str(input(menu).casefold())
    try:
        if opcao == "d":
            valor_deposito = float(input("Escolha o valor a ser depositado:"))

            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Deposito: R$ {valor_deposito:.2f}\n"

            else:
                print("Operação falhou! O valor inserido é inválido!")

        elif opcao == "s":
            valor_saque = float(input("Escolha o valor a ser sacado:"))

            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! O valor do saque é maior que o saldo disponivel!")

            elif excedeu_limite:
                print("Operação falhou! O valo máximo por saque é de R$500,00!")

            elif excedeu_saques:
                print("Operação falhou! O limite diário de saques foi atingido!")

            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor inserido é inválido!")

        elif opcao == "e":
            print(("="*15) + ("Extrato") + ("="*15))
            print("Não foram realizados movimentações" if not extrato else extrato)
            print(f'\n Saldo R$ {saldo:.2f}')
            print(f'='*37)

        elif opcao == "q":
            break

        else:
            print("Operação inválida! Entre com um valor válido!")

    except ValueError:
        print("Operação inválida! Entre com um valor válido!")