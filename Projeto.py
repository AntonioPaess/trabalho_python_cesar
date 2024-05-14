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
            favoritos()
        elif op == "7":
            receita_aleatoria()
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
    favoritas = []

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

    while True:
        print("Receitas Disponíveis:")
        for i, receita in enumerate(receitas, 1):
            print(f"[{i}] - {receita[1].strip()}")

        print("\nMenu de Favoritos:")
        print("[1] - Adicionar Receita aos Favoritos")
        print("[2] - Exibir Favoritos")
        print("[0] - Voltar ao Menu Principal")
        opcao = input("=> ")

        if opcao == "0":
            break
        elif opcao == "1":
            print("Digite o número da receita que deseja adicionar aos favoritos:")
            num_receita = input("=> ")
            try:
                num_receita = int(num_receita)
                if 1 <= num_receita <= len(receitas):
                    nome_receita = receitas[num_receita - 1][1].strip()
                    favoritas.append(nome_receita)
                    print(f"Receita '{nome_receita}' adicionada aos favoritos.")
                else:
                    print("Número de receita inválido. Por favor, escolha um número válido.")
            except ValueError:
                print("Por favor, digite um número válido.")
        elif opcao == "2":
            if not favoritas:
                print("Nenhuma receita favorita adicionada ainda.")
            else:
                print("Receitas Favoritas:")
                for receita in favoritas:
                    print("-", receita)
        else:
            print("Opção Inválida. Por favor, escolha uma opção válida.")

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
        print()
        print(modo_preparo)

def carregar():
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            receitas = []
            for i in arquivo:
                dados = i.strip().split(",")
                receita = {"nome": dados[0], "pais": dados[1], "ingredientes": dados[2].split(','), "modo_preparo": dados[3], "favorita": bool(dados[4])}
                receitas.append(receita)
            return receitas
    except FileNotFoundError:
        return receitas

def excluir_receita(receitas):
    for i, receita in enumerate(receitas, start=1):
        print(f"{i}. {receita['nome']} - {receita['pais']}")
    escolha = int(input("Escolha o número da receita para excluir: "))
    receitas.pop(escolha - 1)
    print(f"A receita '{escolha}' foi excluída com sucesso.")
    with open("receitas.txt", "w", encoding="utf-8") as arquivo:
        for receita in receitas:
            arquivo.write(f"{receita['nome']},{receita['pais']},{','.join(receita['ingredientes'])},{receita['modo_preparo']},{receita['favorita']}\n")


carregar()
menu()
