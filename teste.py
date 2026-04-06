nome = input("Digite o nome: ")

try:
    with open('data/nome.txt', 'r') as arquivo:
        nomes = [linha.strip() for linha in arquivo]
except FileNotFoundError:
    nomes = []

if nome in nomes:
    print("Nome repetido")
else:
    with open('data/nome.txt', 'a') as arquivo:
        arquivo.write(nome + "\n")
    print("Nome salvo com sucesso!")