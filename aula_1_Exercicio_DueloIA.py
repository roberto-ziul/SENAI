## Duelo IA
import random
import time

numero = random.randint(1,5)

print("Bem vindo ao Duelo contra a IA \nEstas são as regras:")
time.sleep(2)
print("-> O programa de vai randomizar um número entre 1 e 5 ")
time.sleep(1)
print("-> O jogador terá no máximo 3 chances para acertar o número!")
time.sleep(1)

print("Agora, insira um número")
for a in range(3):
  resposta = int(input())
  if resposta == numero:
    print("Você acertou o número")
    break
  else:
    print("Você errou o número")

if a == 2:
  print(f"O número era {numero}")
else:
  print("Parabéns!!!")
