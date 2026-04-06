from random import randint

def inserirNome(tipo):
    while 1:
        nome = input(f"Digite o {tipo}: ")
        nome = nome.replace(" ", "")

        if nome.isalpha():
            nome = nome.capitalize()
            return nome
        else:
            print(f"{tipo.capitalize()} Inválido!")

def verificarArquivo(tipo):
    try:
        with open(f'data/{tipo}.txt', 'r') as arquivo:
            nomes = [linha.strip() for linha in arquivo]
    except FileNotFoundError:
        nomes = []
    return nomes

def deletarNome(nome,tipo):
    nomes = verificarArquivo(tipo)
    listaFinal = ""
    if nome in nomes:
        nomes.remove(nome)
        for nome in nomes:
            listaFinal += f'{nome}\n'
        with open(f'data/{tipo}.txt', 'w') as arquivo:
            arquivo.write(listaFinal)
            print(f"{tipo.capitalize()} deletado")
    else:
        print(f"{tipo.capitalize()} não encontrado")

def gerarNomeAleat(nomes,sobrenomes):
    nome = nomes[randint(0,len(nomes)-1)]
    sobrenome = sobrenomes[randint(0,len(sobrenomes)-1)]
    return f'{nome} {sobrenome}'

def clear():
    import os
    os.system("cls")