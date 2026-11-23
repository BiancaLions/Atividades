def comuns(lista1, lista2):
    return [x for x in lista1 if x in lista2]
L1 = [1, 2, 3, 4]
L2 = [3, 4, 5, 6]
print(comuns(L1, L2))