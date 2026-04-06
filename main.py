from metodos import InserirNome, DeletarNome, VerificarArquivo, GerarNomeAleat, Clear

def main():
    rodar = True
    while(rodar):
        Clear()
        try:
            opcao = int(input("[1] Inserir primeiro nome\n[2] Inserir sobrenome\n[3] Deletar \n[4] Gerar nome completo aleatório\n[5] Sair\n[6] Lista Nomes\n -> "))
        
        except ValueError:
            print("Opção Inválida")
            continue

        match opcao:
            case 1:
                nome = InserirNome('nome')
                try:
                    with open('data/nome.txt', 'a') as arquivo:
                        nomes = VerificarArquivo('nome')
                        if nome in nomes:
                            print("Nome Repetido")
                            input()
                        else:
                            arquivo.write(f"{nome}\n")
                            print("Nome Cadastrado")
                            input()
    
                except FileNotFoundError:
                    with open('data/nome.txt', 'w') as arquivo:
                        arquivo.write(nome)
                        print("Nome Cadastrado")
                        input()

            case 2:
                sobrenome = InserirNome('sobrenome')
                try:
                    with open('data/sobrenome.txt', 'a') as arquivo:
                        sobrenomes = VerificarArquivo('sobrenome')
                        if sobrenome in sobrenomes:
                            print("Sobrenome Repetido")
                            input()
                        else:
                            arquivo.write(f"{sobrenome}\n")
    
                except FileNotFoundError:
                    with open('data/sobrenome', 'w') as arquivo:
                        arquivo.write(sobrenome)
                        print("Sobrenome Cadastrado")
                        input()

            case 3:
                try:
                    delete = int(input("[1] Nome\n[2] Sobrenome\n -> "))
                except ValueError:
                    print("Invalido")
                    continue
                if delete == 1:
                    nome = input("Digite o nome: ")
                    nome = nome.capitalize()
                    DeletarNome(nome, 'nome')
                    input()

                elif delete == 2:
                    sobrenome = input("Digite o sobrenome: ")
                    sobrenome = sobrenome.capitalize()
                    DeletarNome(sobrenome, 'sobrenome')
                    input()
                else:
                    print("Inválido")

            case 4:
                nomes = VerificarArquivo('nome')
                sobrenomes = VerificarArquivo('sobrenome')
                nomeGerado = GerarNomeAleat(nomes,sobrenomes)
                print(nomeGerado)
                input()

            case 5:
                rodar = False
                print("Fechando Programa...")

            case 6:
                nomes = VerificarArquivo('nome')
                nomes.sort()
                print("\n".join(nomes))
                input()

if __name__ == '__main__':
    main()