import random
numero = random.randint(1, 50)
tentativas = 0
while True:
    palpite = int(input("Adivinhe o número (1 a 50): "))
    tentativas += 1
    if palpite == numero:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
