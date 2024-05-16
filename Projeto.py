import random

def menu():
    tam = 30
    opcoes = {
        "[1]" : "Cadastrar Receita", # Matheus
        "[2]" : "Visualizar Receitas", # Matheus
        "[3]" : "Atualizar Receita", # Galileu
        "[4]" : "Excluir Receita", # Galileu
        "[5]" : "Filtrar por país", # Thiago 
        "[6]" : "Lista de Favoritos", # Chomp
        "[7]" : "Receita Aleatória", # Chomp
        "[8]" : "Novidade", # Thiago
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
            cadastro()
        elif op == "2":
            receita = input("Digite o nome da receita que deseja visualizar:\n").capitalize()
            visualizar_receita_por_nome(receita)
        elif op == "3":
            pass
        elif op == "4":
            excluir()
        elif op == "5":
            filtrar()
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


def favoritos(): # Check
    favoritas = []

    with open('dados.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        receitas = []
        nova_receita = False
        for linha in linhas:
            if linha.startswith("Nome: "):  # Início de uma nova receita
                if nova_receita:
                    receitas.append(nova_receita)
                nova_receita = {}
                nova_receita["Nome"] = linha.strip()[6:]  # Remove "Nome: " do início da linha
            elif linha.startswith("País de Origem: "):
                nova_receita["País de Origem"] = linha.strip()[16:]
            elif linha.startswith("Ingredientes: "):
                nova_receita["Ingredientes"] = linha.strip()[14:]
            elif linha.startswith("Modo de Preparo: "):
                nova_receita["Modo de Preparo"] = linha.strip()[17:]

        receitas.append(nova_receita)  # Adiciona a última receita

    while True:
        print("Receitas Disponíveis:")
        for i, receita in enumerate(receitas, 1):
            print(f"[{i}] - {receita['Nome']}")

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
                    nome_receita = receitas[num_receita - 1]['Nome']
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



def receita_aleatoria(): # Check
    try:
        with open('dados.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            receitas = []
            nova_receita = False
            ingredientes = ""
            modo_preparo = ""
            for linha in linhas:
                if nova_receita:
                    if 'Modo de Preparo:' in linha:
                        nova_receita = False
                    else:
                        modo_preparo += linha.strip() + '\n'
                elif 'Nome:' in linha:
                    if ingredientes != "":
                        receitas.append((nome, pais_origem, ingredientes, modo_preparo))
                        ingredientes = ""
                        modo_preparo = ""
                    nome = linha.strip().replace('Nome: ', '')
                elif 'País de Origem:' in linha:
                    pais_origem = linha.strip().replace('País de Origem: ', '')
                elif 'Ingredientes:' in linha:
                    ingredientes = linha.strip().replace('Ingredientes: ', '')
                    nova_receita = True

            if ingredientes != "":
                receitas.append((nome, pais_origem, ingredientes, modo_preparo))

            if not receitas:
                print("Não há receitas disponíveis.")
                return

            receita_escolhida = random.choice(receitas)
            nome, pais_origem, ingredientes, modo_preparo = receita_escolhida

            print("Nome:", nome)
            print(f"País de Origem: {pais_origem}\n")
            print(f"Ingredientes:\n{ingredientes}")
    except FileNotFoundError:
        print("O arquivo 'dados.txt' não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro durante a leitura do arquivo:", e)



def excluir(): # Falta Arrumar
    with open('dados.txt', 'r+', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        receitas = []
        for linha in linhas:
            if 'Nome:' in linha:
                nome = linha.split('Nome: ')[1].strip()
            elif 'País de Origem:' in linha:
                pais = linha.split('País de Origem: ')[1].strip()
            elif 'Ingredientes:' in linha:
                ingredientes = linha.split('Ingredientes: ')[1].strip().split(', ')
            elif 'Modo de Preparo:' in linha:
                modo_preparo = linha.split('Modo de Preparo: ')[1].strip()
                receitas.append({'Nome': nome, 'País de Origem': pais, 'Ingredientes': ingredientes, 'Modo de Preparo': modo_preparo})

    while True:
        print("\nReceitas Disponíveis:")
        for i, receita in enumerate(receitas, 1):
            print(f"[{i}] - {receita['Nome']}")

        print("\nMenu de Exclusão:")
        print("[1] - Excluir Receita")
        print("[0] - Voltar ao Menu Principal")
        opcao = input("=> ")

        if opcao == "0":
            break
        elif opcao == "1":
            print("Digite o número da receita que deseja excluir:")
            num_receita = input("=> ")
            try:
                num_receita = int(num_receita)
                if 1 <= num_receita <= len(receitas):
                    del linhas[4*(num_receita-1):4*num_receita]
                    with open('dados.txt', 'w', encoding='utf-8') as arquivo:
                        arquivo.writelines(linhas)
                    print(f"Receita '{receitas[num_receita - 1]['Nome']}' excluída com sucesso.")
                    # Atualiza a lista de receitas após a exclusão
                    del receitas[num_receita - 1]
                else:
                    print("Número de receita inválido. Por favor, escolha um número válido.")
            except ValueError:
                print("Por favor, digite um número válido.")
        else:
            print("Opção Inválida. Por favor, escolha uma opção válida.")



def filtrar(): 
    try:
        with open('dados.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            receitas = []
            nova_receita = None

            for linha in linhas:
                if "Nome: " in linha:
                        if nova_receita:
                            receitas.append(nova_receita) 
                        nova_receita = {"Nome": linha.strip()[6:]}  
                elif "País de Origem: " in linha:
                    nova_receita["País de Origem"] = linha.strip()[16:] 

            if nova_receita:
                receitas.append(nova_receita)  

        pais = input("Digite o país para filtrar as receitas:\n").capitalize()

        receitas_filtradas = [r for r in receitas if r.get("País de Origem", "").lower() == pais.lower()]

        if receitas_filtradas:
            print(f"Receitas do país '{pais}':")
            for receita in receitas_filtradas:
                print(f"{receita['Nome']}")

        else:
            print(f"Não foram encontradas receitas do país '{pais}'.")

    except FileNotFoundError:
        print("O arquivo 'dados.txt' não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro durante a leitura do arquivo:", e)



def cadastro(): # Check
    nome = input("Nome da receita: ").title()
    pais_origem = input("País de origem: ").capitalize()
    ingredientes = input("Ingredientes (separados por vírgula): ").split(',')
    modo_preparo = input("Modo de preparo: ")

    receita = {
        "Nome": nome,
        "País de Origem": pais_origem,
        "Ingredientes": ingredientes,
        "Modo de Preparo": modo_preparo
    }

    with open("dados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("\n")
        for key, value in receita.items():
            arquivo.write(f"{key}: {value}\n")

    print("\nReceita cadastrada com sucesso!\n")



def visualizar_receita_por_nome(nome_busca): # Check
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            receitas = arquivo.read().split("\n\n")
       
        encontrou = False
        for receita in receitas:
            if f"Nome: {nome_busca}" in receita:
                print("Receita encontrada:")
                print(receita)
                encontrou = True
                break
       
        if not encontrou:
            print("Nenhuma receita encontrada com esse nome.")
    except FileNotFoundError:
        print("Nenhuma receita cadastrada ainda.")




menu()
