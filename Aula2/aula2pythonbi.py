idade = int(input('Digite sua idade: '))

print('Daqui 80 anos sua idade será',idade + 80,'anos')

----------------x----------------------------

nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota: '))
media = nota1 + nota2

print('Sua média é de:', media / 2)


----------------x---------------------------

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
peso = float(input('Digite seu peso:'))
altura = float(input('Digite sai altura:'))

imc = peso / (altura * altura)

print('Seu nome é',nome, 'e tem caracteres', len(nome),'você tem' ,idade,'anos e nasceu no ano de',(2024 - idade),'. Você mede', altura,'cm, pesa',peso,' Kg e seu IMC é:',(imc.format) )

----------------x---------------------------

num1 = int(input('Digite um número:'))

if num1 % 2 == 0:
	print('O numero', num1,'é par !')

else:
	print('O numero', num1, 'é impar!')

----------------x---------------------------

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
litros_necessarios = area / 3
latas_necessarias = litros_necessarios / 18
print('Você precisará de', int(latas_necessarias), 'latas de tinta para pintar sua parede.')

----------------x---------------------------

print('Vamos calcular sua média de 2 bimestres')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))


media = nota1 + nota2 + nota3 + nota4

print('Sua média é de:', media / 4)

idade = int(input('Digite sua idade: '))

if idade >= 65:
  print('Você tem gratuidade no transporte!')

else:
	print('Você não tem gratuidade no transporte!')

----------------x---------------------------

idade = int(input('Digite sua idade: '))
idade = 2024

print('Voce tera 80 anos no ano de',idade + 80)

----------------x---------------------------

print('Vamos calcular sua média de notas')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media > 7:
	print('Sua media foi',media,'Voce foi aprovado!')
elif media > 5 and media < 7:
	print('Sua media foi',media,'Voce ficou de recuperacao!')
else:
	print('Sua media foi',media,'e voce está reprovado')

----------------x---------------------------

idade = int(input('Digite sua idade: '))
preco_original = 200

if idade >= 60:
    desconto = idade
elif idade >= 40 and idade < 60:
    desconto = idade / 2
elif idade >= 20 and idade < 40:
    desconto = idade / 4
else:
    desconto = 10

desconto_percentual = (desconto / 100) * preco_original
preco_final = preco_original - desconto_percentual

print('O valor final do óculos é R$', preco_final)
print('O desconto adquirido foi de R$', desconto_percentual)

----------------x---------------------------

salario = float(input('Informe o salário do funcionário: '))

if salario < 1500:
    aumento = salario * 0.25
elif salario >= 1500 and salario <= 1999.99:
    aumento = salario * 0.20
elif salario >= 2000 and salario <= 2999.99:
    aumento = salario * 0.15
elif salario >= 3000 and salario <= 4999.99:
    aumento = salario * 0.10
else:
    aumento = 0

novo_salario = salario + aumento

print('O salário do funcionário era R$ {:.2f}'.format(salario))
print('O aumento foi de R$ {:.2f}'.format(aumento))
print('O novo salário do funcionário é R$ {:.2f}'.format(novo_salario))

