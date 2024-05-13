import random


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
            print(receita_aleatoria())
        elif op == "8":
            pass
        else:
            if op not in opcoes:
                print("Opção Inválida")
                continue

        # print(f"{opcoes.get(op)}\n")



def cadastro():
    pass




def favoritos():
    pass

def receita_aleatoria():
    with open('dados.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        receitas = []
        nova_receita = False
        for linha in linhas:
            if nova_receita:
                ingredientes = linha.strip().split(', ')
                nova_receita = False
            elif ' - ' in linha:
                receitas.append(linha.split(' - ', 1))
                nova_receita = True
        receita_escolhida = random.choice(receitas)
        indice = linhas.index(receita_escolhida[0] + ' - ' + receita_escolhida[1])
        ingredientes = []
        for linha in linhas[indice + 1:]:
            if not linha.strip():
                break
            ingredientes.append(linha.strip())
        indice_modo_preparo = indice + len(ingredientes) + 1
        modo_preparo = ''
        for linha in linhas[indice_modo_preparo + 1:]:
            if not linha.strip():
                break
            modo_preparo += linha.strip() + '\n'
        print("Receita:", receita_escolhida[1].strip())
        for ingrediente in ingredientes:
            print()
            print("- " + ingrediente)
        print()
        print(modo_preparo)





menu()