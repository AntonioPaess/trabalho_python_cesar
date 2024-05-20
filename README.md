<h1 align="center">CRUD em python</h1>

<div align="center" >
<img src="https://github.com/AntonioPaess/trabalho_python_cesar/assets/108696459/00edc9ba-334b-4011-a417-5fdaf124a3fd" alt="Imagem Arredondada" style="width: 100%;  border-radius: 50%; object-fit: cover;">
</div>


# 📢 Descrição do Problema:
Rafael é um entusiasta da culinária e adora experimentar novas receitas de diversos países. No entanto, ele enfrenta dificuldades em organizar suas receitas favoritas e muitas vezes acaba perdendo as que mais gostou. Como um programador dedicado, você decidiu ajudá-lo a criar um sistema de Gerenciamento de Receitas para que Rafael possa manter o controle de suas descobertas gastronômicas.

# 💻 Requisitos funcionais:
1. Cadastro de Receitas: O sistema deve permitir que Rafael cadastre informações
sobre cada receita, incluindo nome, país de origem, ingredientes e modo de preparo.
2. CRUD de Receitas: Rafael deve poder adicionar, visualizar, atualizar e excluir
receitas de sua coleção através de um menu interativo.
3. Filtragem por País: O sistema deve permitir a visualização das receitas de acordo
com o país de origem, facilitando a busca por culinárias específicas.
4. Armazenamento em Banco de Dados: Todas as informações sobre as receitas
devem ser armazenadas em um banco de dados para que persistam além da
execução do programa (arquivo .txt ou .csv).
5. Lista de Favoritos: Rafael deve poder marcar suas receitas favoritas para
acessá-las facilmente em uma lista separada.
6. Sugestão de Receitas Aleatórias: O sistema deve apresentar uma funcionalidade
para sugerir receitas aleatórias de diferentes países, incentivando Rafael a
experimentar novos pratos.
7. Ter pelo menos uma outra funcionalidade a mais que não está descrita aqui neste
documento. Sejam criativos e divirtam-se!

## 📋 Projeto
Este projeto é um gerenciador de receitas que permite cadastrar, visualizar, atualizar, excluir e filtrar receitas por país de origem. Ele também oferece a funcionalidade de listar receitas favoritas e selecionar uma receita aleatória.
# Funcionalidades
## Menu Principal
- O menu principal apresenta as seguintes opções:

- Cadastrar Receita: Permite adicionar uma nova receita ao arquivo dados.txt.
- Visualizar Receitas: Permite visualizar uma receita específica pelo nome.
- Atualizar Receita: Permite atualizar os detalhes de uma receita existente.
- Excluir Receita: Permite excluir uma receita pelo nome.
- Filtrar por país: Permite filtrar receitas pelo país de origem.
- Lista de Favoritos: Permite adicionar receitas à lista de favoritos e exibi-las.
- Receita Aleatória: Seleciona e exibe uma receita aleatória do arquivo.
- Filtrar por Receita: Permite filtrar receitas pelos igredientes.
- Filtrar por Ingrediente: Permite filtrar receitas pelos igredientes.
- Sair: Sai do programa.
## Funcionalidades Detalhadas
Cadastrar Receita
- Cadastra uma nova receita solicitando ao usuário o nome, país de origem, ingredientes e modo de preparo. Os dados são salvos no arquivo dados.txt.

Visualizar Receitas
- Solicita o nome da receita que o usuário deseja visualizar e exibe os detalhes se a receita for encontrada.

Atualizar Receita
- Permite ao usuário atualizar os detalhes de uma receita existente. Solicita o nome da receita a ser atualizada e permite modificar o nome, país de origem, ingredientes e modo de preparo.

Excluir Receita
- Solicita o nome da receita que o usuário deseja excluir e remove a receita do arquivo se encontrada.

Filtrar por País
- Permite ao usuário listar todas as receitas de um país específico.

Lista de Favoritos
- Gerencia uma lista de receitas favoritas. O usuário pode adicionar receitas à lista de favoritos e visualizar as receitas favoritas.

Receita Aleatória
- Seleciona e exibe uma receita aleatória do arquivo dados.txt.

Filtrar por Igredientes
- Permite ao usuário listar todas as receitas que contem um ou mais igredientes específicos.

# 🎲 Arquivo de Dados
Todas as receitas são armazenadas no arquivo dados.txt com o seguinte formato:
Nome: [Nome da Receita]
País de Origem: [País de Origem]
Ingredientes: [Lista de Ingredientes]
Modo de Preparo: [Modo de Preparo]

# Estrutura do Código
Funções
-menu(): Exibe o menu principal e gerencia a navegação entre as opções.
-cadastro(): Cadastra uma nova receita.
-visualizar_receita_por_nome(nome_busca): Visualiza uma receita pelo nome.
-atualizar(): Atualiza uma receita existente.
-excluir(): Exclui uma receita pelo nome.
-filtrar(): Filtra receitas por país de origem.
-favoritos(): Gerencia a lista de receitas favoritas.
-receita_aleatoria(): Seleciona uma receita aleatória do arquivo.
-filtrar_igredientes(): Filtra receitas por igredientes.

# Exemplo de Uso
Para iniciar o programa, basta chamar a função menu():

## 📝 Fluxograma
<div align="center" >
<img src="https://github.com/AntonioPaess/trabalho_python_cesar/assets/108696459/fe2c27ca-9e8b-4af6-ab7f-2c29ffaaa634" alt="Imagem Arredondada" style="width: 900px;">
</div>

## ⚙️ Requisitos
Python 3.6 ou superior.

## 🙋‍♂️ Criado por:
- [Antonios Paes](https://github.com/AntonioPaess)
- [Galileu Moraes](https://github.com/GalileuCMMoares)
- [Matheus Lustosa](https://github.com/MatheusLustosa)
- [Thiago Alves](https://github.com/ThAlvesM)







