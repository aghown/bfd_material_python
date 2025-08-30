# Sistema de catalogacao de livros
while True:
    opcao = input("Escolha uma opção:\n " \
    "1- Adicionar um Livro\n " \
    "2- Editar Informação de um livro cadastrado\n" \
    "3- Pesquisar por um livro\n" \
    "4- Deletar um Livro\n" \
    "0- Sair")

    match opcao:
        case "1":
            print("Adicionando um livro")
        case "2":
            print("Editando um livro")
        case "3":
            print("pesquisando um livro")
        case "4":
            print("deletando um livro")
        case "0":
            break
        case _:
            print("Opção inválida")