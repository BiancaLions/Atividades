with open("texto".txt, "r", encoding="utf-8") as arquivo:
    arquivo.white('Python é uma linguagemde programação.')
with open('texto'.txt, "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    quantidade = len(texto.split())
    print(f"O arquivo possui {quantidade} palavras.")