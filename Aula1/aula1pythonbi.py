import random

palavra_secreta = random.choice(['banana', 'maça', 'laranja', 'uva', 'morango'])
letras_erradas = ''
letras_certas = ''
chances = 6

while chances > 0:
  print('Chances restantes:', chances)
  chute = input('Digite uma letra: ')

  if chute in palavra_secreta:
    print('Acertou!')
    letras_certas += chute
  else:
    print('Errou!')
    letras_erradas += chute
    chances -= 1

  palavra_formada = ''
  for letra in palavra_secreta:
    if letra in letras_certas:
      palavra_formada += letra
    else:
      palavra_formada += '-'

  print('Palavra formada:', palavra_formada)

  if palavra_formada == palavra_secreta:
    print('Você venceu!')
    break

if chances == 0:
  print('Você perdeu!')