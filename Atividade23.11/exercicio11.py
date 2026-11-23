palavra = input('Digite uma palavra: ').lower()
if palavra == palavra[::-1]:
    print('A palavra é um políndromo.')
else:
    print('A palavra não é um políndromo.')