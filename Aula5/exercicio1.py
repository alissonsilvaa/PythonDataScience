'''4)	Crie uma função que receba o nome, idade e CPF e então cadastre como 
um dicionário (dict) em uma lista de usuários.
O programa deverá permitir adicionar usuário, excluir usuário e listar usuários.
Valide se o CPF é válido ou não antes de aceitar o cadastro.'''


usuarios = []

quantidade = 3

nome = input('Nome: ')
idade = int(input('Idade: '))
cpf = int(input('CPF: '))

usuario = {'nome': nome, 'idade': idade, 'CPF': cpf}
usuarios.append(usuario)


opcao = input('''Deseja alterar algum resgistro?Digite
                   1 - alterar registro
                   2 - 
    ''')


if opcao == 'L':

    print('\nDados Cadastrais:')

    for j, item in enumerate(usuarios, start=1):
        print(f"{j} - {item}")


elif opcao == 'R':

    print('\nDados Cadastrais:')
    for k, item in enumerate(usuarios, start=1):
        print(f"{k} - {item}")


    removerIndice = int(input("\nDigite o índice do item que deseja remover: "))


    if 1 <= removerIndice <= len(usuarios):
        del usuarios[removerIndice - 1]
        print(f"\nRegistro deletado cm sucesso: {item}")
        usuarios.sort()

    else:
        print("\nÍndice inválido. Tente novamente.")


elif opcao == 'A':

    novoItem = input("Digite dado que deseja atualizar: ")
    usuarios.append(novo_item)
    print(f"\nItem '{novoItem}'Alteracao realizada com sucesso!")

else:
    print("\nOpção inválida. Tente novamente.")
