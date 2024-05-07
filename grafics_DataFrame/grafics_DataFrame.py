'''Programa que simula uma corrida entre 6 pilotos ao final exibe um gráfico com o melhor tempo de cada piloto'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from re import T

corrida = pd.DataFrame(np.random.uniform(0, 60, size=(6, 10)))

tempo = corrida.sum(axis=1)

corrida


ordemChegada = np.argsort(tempo)
print('---------------------------')

print('Classificação final:\n')
print(f"1º lugar: Piloto {ordemChegada[0]+1} - Tempo total: {tempo[ordemChegada[0]]:.3f}")
print(f"2º lugar: Piloto {ordemChegada[1]+1} - Tempo total: {tempo[ordemChegada[1]]:.3f}")
print(f"3º lugar: Piloto {ordemChegada[2]+1} - Tempo total: {tempo[ordemChegada[2]]:.3f}")
print(f"4º lugar: Piloto {ordemChegada[3]+1} - Tempo total: {tempo[ordemChegada[3]]:.3f}")
print(f"5º lugar: Piloto {ordemChegada[4]+1} - Tempo total: {tempo[ordemChegada[4]]:.3f}")
print(f"6º lugar: Piloto {ordemChegada[5]+1} - Tempo total: {tempo[ordemChegada[5]]:.3f}")

melhor_volta = corrida.min(axis=0)
melhor_volta = np.min(corrida)
piloto_melhor_volta = np.argmin(corrida)
print()
print('A melhor volta foi a',piloto_melhor_volta)
print('O tempo foi:',round(melhor_volta, 4))
print('A volta com menor tempo foi:',piloto_melhor_volta%10)
print('O piloto foi',piloto_melhor_volta//10)
'''ordemChegada = pd.DataFrame({'Piloto': [melhor_volta],'Tempo': [piloto_melhor_volta]}, index=[10, 20, 30, 40, 50, 60])
lines = ordemChegada.plot.line()'''


plt.figure(figsize=(10, 6))
plt.title('Classificação dos Pilotos')
plt.xlabel('Piloto')
plt.ylabel('Tempo Total')
plt.xticks(np.arange(6), [f'Piloto {i+1}' for i in range(6)])


plt.bar(np.arange(6), tempo)

for i, bar in enumerate(plt.gca().patches):
    plt.gca().text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                   str(round(tempo[i], 2)), ha='center', va='bottom')

plt.show()