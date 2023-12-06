menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor_deposito = float(input('Quando deseja depositar? '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f'Depósito: + R$ {valor_deposito:.2f}')
            print('Depósito realizado com sucesso!')
        else:
            print('Por favor, insira um valor de depósito válido (positivo)!')
    
    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input('Quanto deseja sacar? '))
            if valor_saque > 0:
                if 500 >= valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato.append(f'Saque: - R$ {valor_saque:.2f}')
                    print('Saque realizado com sucesso!')
                    numero_saques += 1
                elif valor_saque > saldo:
                    print('Saldo insuficiente!')
                else:
                    print('Valor maior do que o limite permitido!')
            else:
                print('Por favor, insira um valor de saque válido (positivo)!')
        else:
            print('Limite de saque diario excedido!')
           
    elif opcao == 'e':
        for operacao in extrato:
            print(operacao)
        print(f'\nSaldo: R$ {saldo:.2f}')
    
    elif opcao == 'q':
        print('Operação finalizada!')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')