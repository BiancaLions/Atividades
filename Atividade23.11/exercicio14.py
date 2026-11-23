numeros = input('Digite 5 números separados por espaço: ').split()
numeros = [int(num) for num in numeros]
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")