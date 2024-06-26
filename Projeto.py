import random
import os
os.system('cls')

def menu():
    tam = 30
    opcoes = {
        "[1]" : "Cadastrar Receita", 
        "[2]" : "Visualizar Receitas", 
        "[3]" : "Atualizar Receita", 
        "[4]" : "Excluir Receita", 
        "[5]" : "Filtrar por país", 
        "[6]" : "Lista de Favoritos", 
        "[7]" : "Receita Aleatória", 
        "[8]" : "Filtrar por ingredientes", 
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
            os.system('cls')
            receita = input("Digite o nome da receita que deseja visualizar:\n").capitalize()
            visualizar_receita_por_nome(receita)
        elif op == "3":
            atualizar()
        elif op == "4":
            excluir()
        elif op == "5":
            filtrar()
        elif op == "6":
            favoritos()
        elif op == "7":
            receita_aleatoria()
        elif op == "8":
            filtrar_ingredientes()
        else:
            if op not in opcoes:
                print("Opção Inválida")
                continue




def cadastro(): 
    os.system('cls')
    nome = input("Nome da receita: ").title()
    pais_origem = input("País de origem: ").capitalize()
    ingredientes = input("Ingredientes (separados por vírgula sem espaço): ").split(',')
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
    
    os.system('cls')
    print("\nReceita cadastrada com sucesso!\n")



def visualizar_receita_por_nome(nome_busca): # Check
    os.system('cls')
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            receitas = arquivo.read().strip().split("\n\n")
       
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


def atualizar():
    os.system('cls')
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            receitas = arquivo.read().strip().split("\n\n")

        nome_atualizar = input("Digite o nome da receita que deseja atualizar:\n").title().strip()
        encontrou = False
        os.system('cls')

        for i, receita in enumerate(receitas):
            lines = receita.split("\n")
            for line in lines:
                if nome_atualizar.lower() in line.lower(): 
                    encontrou = True
                    print("Receita encontrada:")
                    print(receita)

                    novo_nome = input(f"\nNovo nome da receita (pressione Enter para manter o mesmo): ").title().strip()
                    novo_pais_origem = input("Novo país de origem (pressione Enter para manter o mesmo): ").capitalize().strip()
                    novos_ingredientes = input("Novos ingredientes (separados por vírgula, pressione Enter para manter os mesmos): ").strip().split(',')
                    novo_modo_preparo = input("Novo modo de preparo (pressione Enter para manter o mesmo): ").strip()

                    receita_atualizada = []

                    for linha in receita.split("\n"):
                        if "Nome: " in linha and novo_nome:
                            linha = f"Nome: {novo_nome}"
                        elif "País de Origem: " in linha and novo_pais_origem:
                            linha = f"País de Origem: {novo_pais_origem}"
                        elif "Ingredientes: " in linha and novos_ingredientes:
                            linha = f"Ingredientes: {novos_ingredientes}"
                        elif "Modo de Preparo: " in linha and novo_modo_preparo:
                            linha = f"Modo de Preparo: {novo_modo_preparo}"
                        receita_atualizada.append(linha)

                    receitas[i] = "\n".join(receita_atualizada)
                    break 
            if encontrou:
                break  
        
        os.system('cls')
        if encontrou:
            with open("dados.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("\n\n".join(receitas) + "\n")
            print(f"A receita '{nome_atualizar}' foi atualizada com sucesso.")
        else:
            print(f"Nenhuma receita encontrada com o nome '{nome_atualizar}'.")

    except FileNotFoundError:
        print("O arquivo 'dados.txt' não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro durante a leitura do arquivo:", e)


def excluir():
    os.system('cls')
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        receitas = []
        nova_receita = []
        for linha in linhas:
            if linha.strip() == "" and nova_receita:
                receitas.append("\n".join(nova_receita).strip())
                nova_receita = []
            else:
                nova_receita.append(linha.strip())
        
        if nova_receita:
            receitas.append("\n".join(nova_receita).strip())

        nome_excluir = input("Digite o nome da receita que deseja excluir:\n").title()
        encontrou = False
        novas_receitas = []

        for receita in receitas:
            if receita.startswith(f"Nome: {nome_excluir}"):
                print("Receita encontrada e excluída:")
                print(receita)
                encontrou = True
            else:
                novas_receitas.append(receita)

        if encontrou:
            with open("dados.txt", "w", encoding="utf-8") as arquivo:
                for receita in novas_receitas:
                    arquivo.write(receita + "\n\n")
            print(f"A receita '{nome_excluir}' foi excluída com sucesso.")
        else:
            print(f"Nenhuma receita encontrada com o nome '{nome_excluir}'.")

    except FileNotFoundError:
        print("O arquivo 'dados.txt' não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro durante a leitura do arquivo:", e)



def filtrar():
    os.system('cls') 
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
        
        os.system('cls')
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



def favoritos():  
    os.system('cls')
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
            os.system('cls')
            break
        elif opcao == "1":
            print("Digite o número da receita que deseja adicionar aos favoritos:")
            num_receita = input("=> ")
            try:
                num_receita = int(num_receita)
                if 1 <= num_receita <= len(receitas):
                    nome_receita = receitas[num_receita - 1]['Nome']
                    favoritas.append(nome_receita)
                    os.system('cls')
                    print(f"Receita '{nome_receita}' adicionada aos favoritos.")
                else:
                    os.system('cls')
                    print("Número de receita inválido. Por favor, escolha um número válido.")
            except ValueError:
                os.system('cls')
                print("Por favor, digite um número válido.")
        elif opcao == "2":
            if not favoritas:
                os.system('cls')
                print("Nenhuma receita favorita adicionada ainda.")
            else:
                os.system('cls')
                print("Receitas Favoritas:")
                for receita in favoritas:
                    print("-", receita)
        else:
            os.system('cls')
            print("Opção Inválida. Por favor, escolha uma opção válida.")



def receita_aleatoria(): # Check
    os.system('cls')
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            receitas = arquivo.read().split("\n\n")
        
        if not receitas:
            print("Não há receitas disponíveis.")
            return

        receita_mod = random.choice(receitas)

        encontrou = False
        for receita in receitas:
            if receita == receita_mod:
                print("Receita aleatória:")
                print(receita_mod)
                encontrou = True
                break

        if not encontrou:
            print("Nenhuma receita encontrada.")
    except FileNotFoundError:
        print("Nenhuma receita cadastrada ainda.")
    except Exception as e:
        print("Ocorreu um erro durante a leitura do arquivo:", e)



def filtrar_ingredientes():
    os.system('cls')
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
                elif "Ingredientes: " in linha:
                    ingredientes = linha.strip()[14:].strip("[]").replace("'", "").split(", ")
                    nova_receita["Ingredientes"] = [ingrediente.lower() for ingrediente in ingredientes]

            if nova_receita:
                receitas.append(nova_receita)
        
        ingredientes_input = input("Digite os ingredientes para filtrar as receitas (separados por vírgula):\n").lower().split(',')
        
        receitas_filtradas = []
        for receita in receitas:
            if "Ingredientes" in receita:
                ingredientes_receita = receita["Ingredientes"]
                if all(ingrediente in ingredientes_receita for ingrediente in ingredientes_input):
                    receitas_filtradas.append(receita)
        
        os.system('cls')    
        if receitas_filtradas:
            print("Receitas que contêm os ingredientes especificados:")
            for receita in receitas_filtradas:
                print(f"{receita['Nome']}")
        else:
            print("Nenhuma receita encontrada com os ingredientes especificados.")

    except FileNotFoundError:
        print("O arquivo 'dados.txt' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante a leitura do arquivo: {e}")

menu()
