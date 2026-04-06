from metodos import inserirNome, deletarNome, verificarArquivo, gerarNomeAleat, clear
from time import sleep

def main():
    rodar = True
    while(rodar):
        clear()
        print("----------MENU----------")
        try:
            opcao = int(input("[1] Inserir primeiro nome\n[2] Inserir sobrenome\n[3] Deletar \n[4] Gerar nome completo aleatório\n[5] Sair\n[6] Lista Nomes\n -> "))
        
        except ValueError:
            print("Opção Inválida")
            sleep(2)
            continue

        match opcao:
            case 1:
                nome = inserirNome('nome')
                try:
                    with open('data/nome.txt', 'a') as arquivo:
                        nomes = verificarArquivo('nome')
                        if nome in nomes:
                            print("Nome Repetido")
                            sleep(2)
                        else:
                            arquivo.write(f"{nome}\n")
                            print("Nome Cadastrado")
                            sleep(2)
    
                except FileNotFoundError:
                    with open('data/nome.txt', 'w') as arquivo:
                        arquivo.write(nome)
                        print("Nome Cadastrado")
                        sleep(2)

            case 2:
                sobrenome = inserirNome('sobrenome')
                try:
                    with open('data/sobrenome.txt', 'a') as arquivo:
                        sobrenomes = verificarArquivo('sobrenome')
                        if sobrenome in sobrenomes:
                            print("Sobrenome Repetido")
                            sleep(2)
                        else:
                            arquivo.write(f"{sobrenome}\n")
    
                except FileNotFoundError:
                    with open('data/sobrenome', 'w') as arquivo:
                        arquivo.write(sobrenome)
                        print("Sobrenome Cadastrado")
                        sleep(2)

            case 3:
                try:
                    delete = int(input("[1] Nome\n[2] Sobrenome\n -> "))
                except ValueError:
                    print("Invalido")
                    sleep(2)
                    continue
                if delete == 1:
                    nome = input("Digite o nome: ")
                    nome = nome.capitalize()
                    deletarNome(nome, 'nome')
                    sleep(2)

                elif delete == 2:
                    sobrenome = input("Digite o sobrenome: ")
                    sobrenome = sobrenome.capitalize()
                    deletarNome(sobrenome, 'sobrenome')
                    sleep(2)
                else:
                    print("Inválido")
                    sleep(2)
            case 4:
                nomes = verificarArquivo('nome')
                sobrenomes = verificarArquivo('sobrenome')
                nomeGerado = gerarNomeAleat(nomes,sobrenomes)
                print(nomeGerado)
                input()

            case 5:
                rodar = False
                print("Fechando Programa...")

            case 6:
                nomes = verificarArquivo('nome')
                nomes.sort()
                print("\n".join(nomes))
                input()

            case _:
                print("Opção Inválida")
                sleep(2)

if __name__ == '__main__':
    main()