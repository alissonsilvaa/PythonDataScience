'''

Faça um jogo de batalha entre você e o computador:
Cada um dos jogadores inicia com 10 pontos de vida.
Neste jogo você deverá comparar o poder de combate em cada turno, quem ganhar
 desfere o ataque no oponente causando o dano respectivo.
Você tem dois ataques, que poderá selecionar no início de cada rodada:
1.	Cabeçada: Tem poder de combate 3, se ganhar tira 3 de vida do oponente e
toma 1 de dano.
2.	Soco: Tem poder de combate aleatório (jogar no dado D6) e caso ganhe causa
dano aleatório (jogar no dado D6).
O computador tem apenas o ataque Soco.
Quem chegar a 0 pontos de vida perde o jogo.'''

import random

# Inicialização dos pontos de vida
humano = 20
chatGPT = 20

# Loop principal do jogo
round = 1
while humano > 0 and chatGPT > 0:
    acao_humano = random.randint(1, 6)
    acao_chatGPT = random.randint(1, 6)
    print(f"Round {round}")  # Exibe o round atual
    print(f"Humano: {humano}")
    print(f"ChatGPT: {chatGPT}")
    print()




    escolha = input('Digite 1 para cabeçada ou 2 para soco (ataque): ')

    if acao_humano > acao_chatGPT:
        print('Você acertou!')

        if escolha == "1":
            # Cabeçada
            humano -= 1
            chatGPT -= 3
            print("Você deu uma cabeçada no ChatGPT!")
        elif escolha == "2":
            # Soco
            seu_dano = random.randint(1, 6)
            computador_dano = random.randint(1, 6)
            humano -= computador_dano
            chatGPT -= seu_dano
            print(f"Humano causou {seu_dano} de dano ao ChatGPT.")
            print(f"O ChatGPT causou {computador_dano} de dano ao Humano.")
        else:
            print("Opção inválida. Escolha 1 para cabeçada ou 2 para soco.")

        round += 1  # Incrementa o round a cada volta

    else:

        print('Você perdeu ! O computador te deu um soco.')
        seu_dano = random.randint(1, 6)
        computador_dano = random.randint(1, 6)
        humano -= computador_dano
        chatGPT -= seu_dano
        print(f"Humano sofreu {computador_dano} de dano.")
        print(f"O ChatGPT causou {seu_dano} de dano ao Humano.")

        round += 1  # Incrementa o round a cada volta

    print()  # Linha em branco para melhorar a visualização

# Verificação do vencedor
if humano <= 0:
    print("Humano perdeu! O ChatGPT venceu.")
else:
    print("Parabéns! O Humano venceu o ChatGPT.")