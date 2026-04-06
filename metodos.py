from random import randint

def InserirNome(tipo):
    while 1:
        nome = input(f"Digite o {tipo}: ")
        nome = nome.replace(" ", "")

        if nome.isalpha():
            nome = nome.capitalize()
            break
        else:
            print(f"{tipo.capitalize()} Inválido!")

    return nome

def VerificarArquivo(tipo):
    try:
        with open(f'data/{tipo}.txt', 'r') as arquivo:
            nomes = [linha.strip() for linha in arquivo]
    except FileNotFoundError:
        nomes = []
    return nomes

def DeletarNome(nome,tipo):
    nomes = VerificarArquivo(tipo)
    listaFinal = ""
    if nome in nomes:
        nomes.remove(nome)
        for nome in nomes:
            listaFinal += f'{nome}\n'
        with open(f'data/{tipo}.txt', 'w') as arquivo:
            arquivo.write(listaFinal)
            print("DELETADO")
    else:
        print(f"{tipo.capitalize()} não encontrado")

def GerarNomeAleat(nomes,sobrenomes):
    nome = nomes[randint(1,len(nomes)-1)]
    sobrenome = sobrenomes[randint(1,len(sobrenomes)-1)]
    return f'{nome} {sobrenome}'

def Clear():
    import os
    os.system("cls")