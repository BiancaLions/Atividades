lista = []
def adicionar('nome'):
    lista.append('nome')
    print(f"{nome} adicionado(a).")
def listar():
    print("Nomes cadastrados:")
    for n in lista:
        print(n)
def remover(nome):
    if nome in lista:
        lista.remove(nome)
        print(f"{nome} removido(a).")
    else:
        print(f"{nome} não encontrado(a).")
while True:
    print("\n1 - Adicionar\n2 - Listar\n3 - Remover\n4 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome para adicionar: ")
        adicionar(nome)
    elif opcao == "2":
        listar()
    elif opcao == "3":
        nome = input("Digite o nome para remover: ")
        remover(nome)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
