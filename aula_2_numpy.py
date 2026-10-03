#Utilização da biblioteca numpy para calcular lista
import numpy as np #as = alias | chame a lib "numpy" como "np"

print("Python Puro")
precos_lista = [100_000, 200_000, 300_000]

print("Lista vezes 2:", precos_lista * 2)

print("\nSolução NUMPY")
precos_numpy = np.array([100_000, 200_000, 300_000])

precos_atualizados = precos_numpy * 2
print("Array vezes 2:", precos_atualizados)

matriz_dados = np.array([
  [1, 2, 3],
  [4, 5, 6]
])

print(matriz_dados)

#################################################################
#################################################################

# Operações Matemáticas e Estatíscas com NumPy
dados = np.array([10, 20, 30, 40, 50])

print("Soma de todos os elementos:", dados.sum())
print("Média aritmética:", dados.mean())
print("Desvio padrão:", dados.std().round(2))
print("Valor mínimo:", dados.min())
print("Valor máximo:", dados.max())
