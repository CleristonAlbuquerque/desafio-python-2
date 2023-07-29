import random

# Mensagem de boas-vindas
print("Olá Usuário, Seja Bem Vindo!")
print('\n')

# Menu de operações
menu_operacao = '''
O que você deseja realizar:

[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Cadastrar Usuário
[5] - Criar uma Conta
[6] - Sair
'''

# Variáveis de controle
saldo = 0
limite = 500
extrato = []  # Lista para armazenar o extrato das operações
numero_saques = 0
LIMITE_SAQUE = 3
usuario = {'Nome': None,
           'CPF': None,
           'Endereço': None,
           'Agência': None,
           'Conta-Corrente': None,
           'Password': None
           } # Dicionário vazio

def cadastrar_usuario(usuario):
    try:
        cpf = int(input('Insira o cpf: '))
        if cpf == usuario['CPF']:
            print('Usuário já cadastrado')
        else:
            usuario['CPF'] = cpf
            usuario['Nome'] = input('Insira o nome: ')
            usuario['Endereço'] = input('Insira o endereço: ')
            print(f"{usuario['Nome']}, cadastro realizado com sucesso!")
    except ValueError:
        print('CPF deve ser um número')

def criar_conta(usuario):
    try:
        user_conta = int(input("Insira o cpf: "))
        if user_conta == usuario['CPF']:
            opcao = input('Deseja criar uma conta? (sim ou não): ')
            if opcao.lower() == 'sim':
                usuario['Agência'] = '0001'
                usuario['Conta-Corrente'] =  random.randint(100000, 999999)
                while True:
                    usuario['Password'] = int(input('Insira a senha (apenas números): '))
                    repita = int(input('Repita a senha: '))
                    if repita == usuario['Password']:
                        print('Conta criada com sucesso!')
                        print(f'Agência: {usuario["Agência"]}, Conta-Corrente: {usuario["Conta-Corrente"]}')
                        break
                    else:
                        print('As senhas não correspondem. Tente novamente.')
        else:
            print('CPF não encontrado')
    except ValueError:
        print('Entrada inválida. Tente novamente.')

def realizar_deposito(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f'Depósito R$ {valor:.2f}')
        else:
            print('O valor informado é inválido')
    except ValueError:
        print('Insira um valor numérico válido.')
    return saldo, extrato

def realizar_saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUE):
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print('O valor informado é inválido.')
        elif valor > saldo:
            print('Saldo insuficiente. Verifique seu saldo antes de fazer o saque.')
        elif valor > limite:
            print('O valor do saque excedeu o limite diário.')
        elif numero_saques >= LIMITE_SAQUE:
            print('Número máximo de saques diários atingido.')
        else:
            saldo -= valor
            extrato.append(f'Saque R$ {valor:.2f}')
            numero_saques += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
    except ValueError:
        print('Insira um valor numérico válido.')
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print('========= Extrato ==========')
    if extrato:
        for movimentacao in extrato:
            print(movimentacao)
    else:
        print('Não foram realizadas movimentações.')
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('============================')

while True:
    opcao = input(menu_operacao)

    if opcao == '1':
        saldo, extrato = realizar_deposito(saldo, extrato)
    elif opcao == '2':
        saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUE)
    elif opcao == '3':
        mostrar_extrato(saldo, extrato)
    elif opcao == '4':
        cadastrar_usuario(usuario)
    elif opcao == '5':
        criar_conta(usuario)
    elif opcao == '6':
        print('Aguarde!....')
        print('Você está saindo do ambiente.')
        break
    else:
        print('Operação inválida, por favor selecione a operação desejada')





