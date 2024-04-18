import re

'''Crie um programa para inserir, apagar e listar os itens de uma lista de
compras (utilize append e pop/del).'''

lista_de_compras = []

quantidade_itens = 2

print('Digite os itens da lista de compras')
for i in range(quantidade_itens):
    novo_item = input('Item ' + str(i + 1) + ': ')
    lista_de_compras.append(novo_item)

opcao = input("O que você deseja fazer? Digite A para adicionar, R para remover, L para listar: ")


if opcao == 'L':

    print('\nLista de Compras:')

    for j, item in enumerate(lista_de_compras, start=1):
        print(f"{j} - {item}")


elif opcao == 'R':

    print('\nLista de Compras:')
    for k, item in enumerate(lista_de_compras, start=1):
        print(f"{k} - {item}")


    removerIndice = int(input("\nDigite o índice do item que deseja remover: "))


    if 1 <= removerIndice <= len(lista_de_compras):
        del lista_de_compras[removerIndice - 1]
        print(f"\nItem removido: {item}")
        lista_de_compras.sort()

    else:
        print("\nÍndice inválido. Tente novamente.")


elif opcao == 'A':

    novoItem = input("Digite o novo item a ser adicionado: ")
    lista_de_compras.append(novo_item)
    print(f"\nItem '{novoItem}' adicionado à lista!")

else:
    print("\nOpção inválida. Tente novamente.")