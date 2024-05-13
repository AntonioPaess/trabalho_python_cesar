def menu():
    tam = 30
    opcoes = {
        "[1]" : "Cadastrar Receita", # Matheus
        "[2]" : "Visualizar Receitas", # Matheus
        "[3]" : "Atualizar Receita", # Galileu
        "[4]" : "Excluir Receita", # Galileu
        "[5]" : "Filtrar por país", 
        "[6]" : "Lista de Favoritos", # Chomp
        "[7]" : "Receita Aleatória", # Chomp
        "[8]" : "Novidade",
        "[0]" : "Sair"
    }
    while True:
        print(f"+{"-"* tam}+")
        print(f"|{"MENU":^{tam}}|")
        print(f"+{"-"* tam}+")
        for k, v in opcoes.items():
            print(f"|{f'{k} - {v}':{tam}}|")
        print(f"+{'-' * tam}+")

        op = input("=> ")

        if op not in opcoes:
            print("Opção Inválida")
            continue
        if op == "0":
            break
        elif op == "1":
            pass
        elif op == "2":
            pass
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "5":
            pass
        elif op == "6":
            pass
        elif op == "7":
            pass
        elif op == "8":
            pass


        print(f"{opcoes.get(op)}\n")



def cadastro():




menu()