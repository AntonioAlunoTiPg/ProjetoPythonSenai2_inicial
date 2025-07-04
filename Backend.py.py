import sqlite3 ## Importa a biblioteca sqlite3 para interagir com bancos de dados SQLite.


def criar_conexao(): ## Define a função para criar uma conexão com o banco de dados.
    """ ## Início da docstring da função criar_conexao.
    Cria e retorna uma conexão com o banco de dados SQLite 'agenda.db'.

    Se o banco de dados não existir, ele será criado.

    Returns:
        sqlite3.Connection: Objeto de conexão com o banco de dados.
    """ ## Fim da docstring da função criar_conexao.
    return sqlite3.connect("agenda.db") ## Retorna um objeto de conexão ao banco de dados 'agenda.db'.


## Estrutura do Banco de Dados ## Título de seção para a estrutura do banco de dados.


def criar_tabela(): ## Define a função para criar a tabela de contatos.
    """ ## Início da docstring da função criar_tabela.
    Cria a tabela 'contatos' no banco de dados, se ela ainda não existir.

    A tabela inclui os campos:
    - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    - nome (TEXT NOT NULL)
    - telefone (TEXT NOT NULL)
    - cpf (TEXT, pode ser NULL)
    - endereco (TEXT, pode ser NULL)
    """ ## Fim da docstring da função criar_tabela.
    conexao = criar_conexao() ## Chama a função para criar uma conexão com o banco de dados.
    cursor = conexao.cursor() ## Cria um objeto cursor para executar comandos SQL.
    cursor.execute(""" ## Inicia a execução de um comando SQL multilinha.
        CREATE TABLE IF NOT EXISTS contatos ( ## Cria a tabela 'contatos' se ela não existir.
            id INTEGER PRIMARY KEY AUTOINCREMENT, ## Define a coluna 'id' como chave primária, inteira e auto-incrementável.
            nome TEXT NOT NULL, ## Define a coluna 'nome' como texto e não nula.
            telefone TEXT NOT NULL, ## Define a coluna 'telefone' como texto e não nula.
            cpf TEXT, ## Define a coluna 'cpf' como texto (pode ser nula).
            endereco TEXT ## Define a coluna 'endereco' como texto (pode ser nula).
        )
    """) ## Fim do comando SQL.
    conexao.commit() ## Confirma as alterações no banco de dados.
    conexao.close() ## Fecha a conexão com o banco de dados.


## Funções de Manipulação de Contatos ## Título de seção para as funções de manipulação de contatos.


def adicionar_contato(nome, telefone, cpf, endereco): ## Define a função para adicionar um novo contato.
    """ ## Início da docstring da função adicionar_contato.
    Adiciona um novo contato à tabela 'contatos'.

    Args:
        nome (str): O nome do contato.
        telefone (str): O número de telefone do contato.
        cpf (str): O CPF do contato (pode ser uma string vazia para NULL).
        endereco (str): O endereço do contato (pode ser uma string vazia para NULL).
    """ ## Fim da docstring da função adicionar_contato.
    conexao = criar_conexao() ## Chama a função para criar uma conexão com o banco de dados.
    cursor = conexao.cursor() ## Cria um objeto cursor.
    cursor.execute( ## Inicia a execução de um comando SQL.
        "INSERT INTO contatos (nome, telefone, cpf, endereco) VALUES (?, ?, ?, ?)", ## Insere dados na tabela 'contatos'.
        (nome, telefone, cpf, endereco) ## Fornece os valores para a inserção.
    )
    conexao.commit() ## Confirma as alterações.
    conexao.close() ## Fecha a conexão.
    print("Contato adicionado com sucesso!") ## Imprime uma mensagem de sucesso.


def listar_contatos(): ## Define a função para listar todos os contatos.
    """ ## Início da docstring da função listar_contatos.
    Lista todos os contatos presentes na tabela 'contatos'.

    Exibe ID, Nome, Telefone, CPF e Endereço de cada contato.
    Se os campos de CPF ou Endereço estiverem vazios no banco,
    'N/A' será exibido no lugar.
    """ ## Fim da docstring da função listar_contatos.
    conexao = criar_conexao() ## Chama a função para criar uma conexão.
    cursor = conexao.cursor() ## Cria um objeto cursor.
    cursor.execute("SELECT * FROM contatos") ## Seleciona todas as colunas de todos os contatos.
    contatos = cursor.fetchall() ## Busca todos os resultados da query.
    if contatos: ## Verifica se há contatos na lista.
        print("\n--- Lista de Contatos ---") ## Imprime um cabeçalho para a lista.
        for contato in contatos: ## Itera sobre cada contato retornado.
            ## Acessa os campos pelos índices da tupla resultante da query. ## Comentário sobre acesso aos campos.
            ## Usa 'or "N/A"' para mostrar "N/A" se o valor no banco for NULL (None em Python). ## Comentário sobre tratamento de valores nulos.
            print( ## Imprime as informações do contato formatadas.
                f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, " ## Formata e imprime ID, Nome e Telefone.
                f"CPF: {contato[3] or 'N/A'}, Endereço: {contato[4] or 'N/A'}" ## Formata e imprime CPF e Endereço, com 'N/A' para nulos.
            )
        print("-------------------------") ## Imprime um rodapé para a lista.
    else: ## Se não houver contatos.
        print("Nenhum contato encontrado.") ## Imprime uma mensagem indicando que nenhum contato foi encontrado.
    conexao.close() ## Fecha a conexão.


def buscar_contato_por_nome(nome): ## Define a função para buscar contatos por nome.
    """ ## Início da docstring da função buscar_contato_por_nome.
    Busca contatos na tabela 'contatos' por uma parte do nome e exibe suas informações.

    A busca é case-insensitive para SQLite.
    Exibe 'N/A' se os campos de CPF ou Endereço estiverem vazios.

    Args:
        nome (str): A parte do nome a ser buscada.
    """ ## Fim da docstring da função buscar_contato_por_nome.
    conexao = criar_conexao() ## Chama a função para criar uma conexão.
    cursor = conexao.cursor() ## Cria um objeto cursor.
    ## Usa LIKE e % para permitir busca por parte do nome (case-insensitive para SQLite). ## Comentário sobre a busca LIKE.
    cursor.execute("SELECT * FROM contatos WHERE nome LIKE ?", ('%' + nome + '%',)) ## Executa a busca por nome usando LIKE.
    resultados = cursor.fetchall() ## Busca todos os resultados da query.
    if resultados: ## Verifica se há resultados.
        print(f"\n--- Resultados da Busca por '{nome}' ---") ## Imprime um cabeçalho para os resultados da busca.
        for resultado in resultados: ## Itera sobre cada resultado.
            print( ## Imprime as informações do contato formatadas.
                f"ID: {resultado[0]}, Nome: {resultado[1]}, Telefone: {resultado[2]}, " ## Formata e imprime ID, Nome e Telefone.
                f"CPF: {resultado[3] or 'N/A'}, Endereço: {resultado[4] or 'N/A'}" ## Formata e imprime CPF e Endereço, com 'N/A' para nulos.
            )
        print("---------------------------------------") ## Imprime um rodapé para os resultados.
    else: ## Se nenhum resultado for encontrado.
        print(f"Nenhum contato encontrado com o nome '{nome}'.") ## Imprime uma mensagem de nenhum contato encontrado.
    conexao.close() ## Fecha a conexão.


def remover_contato_por_id(contato_id): ## Define a função para remover um contato por ID.
    """ ## Início da docstring da função remover_contato_por_id.
    Remove um contato da tabela 'contatos' pelo seu ID.

    Args:
        contato_id (int): O ID do contato a ser removido.
    """ ## Fim da docstring da função remover_contato_por_id.
    conexao = criar_conexao() ## Chama a função para criar uma conexão.
    cursor = conexao.cursor() ## Cria um objeto cursor.
    cursor.execute("DELETE FROM contatos WHERE id = ?", (contato_id,)) ## Executa o comando SQL para deletar o contato pelo ID.
    conexao.commit() ## Confirma a remoção.
    conexao.close() ## Fecha a conexão.
    print("Contato removido com sucesso!") ## Imprime uma mensagem de sucesso.


## Menu Principal ## Título de seção para o menu principal.


def menu(): ## Define a função para exibir o menu principal e gerenciar as opções.
    """ ## Início da docstring da função menu.
    Exibe o menu principal da agenda e gerencia as interações do usuário.

    Garante que a tabela de contatos seja criada (ou atualizada se o DB for novo)
    antes de exibir o menu.
    """ ## Fim da docstring da função menu.
    criar_tabela() ## Garante que a tabela de contatos exista antes de exibir o menu.

    while True: ## Inicia um loop infinito para o menu.
        print("\n   --- Menu da Agenda ---") ## Imprime o cabeçalho do menu.
        print("1 - Adicionar contato") ## Opção para adicionar contato.
        print("2 - Listar contatos") ## Opção para listar contatos.
        print("3 - Buscar contato por nome") ## Opção para buscar contato.
        print("4 - Remover contato por ID") ## Opção para remover contato.
        print("5 - Sair") ## Opção para sair.
        print("------------------------") ## Imprime um separador.
        opcao = input("Escolha uma opção: ") ## Solicita ao usuário que escolha uma opção.

        if opcao == "1": ## Verifica se a opção escolhida é "1" (Adicionar contato).
            nome = input("Nome: ") ## Solicita o nome do contato.
            telefone = input("Telefone: ") ## Solicita o telefone do contato.
            cpf = input("CPF (opcional, ex: 123.456.789-00): ") ## Solicita o CPF do contato (opcional).
            endereco = input("Endereço (opcional, ex: Rua A, 123, Bairro X): ") ## Solicita o endereço do contato (opcional).
            adicionar_contato(nome, telefone, cpf, endereco) ## Chama a função para adicionar o contato.
        elif opcao == "2": ## Verifica se a opção escolhida é "2" (Listar contatos).
            listar_contatos() ## Chama a função para listar os contatos.
        elif opcao == "3": ## Verifica se a opção escolhida é "3" (Buscar contato por nome).
            nome = input("Digite o nome (ou parte dele) para buscar: ") ## Solicita a parte do nome para buscar.
            buscar_contato_por_nome(nome) ## Chama a função para buscar o contato por nome.
        elif opcao == "4": ## Verifica se a opção escolhida é "4" (Remover contato por ID).
            try: ## Inicia um bloco try para tratamento de erros.
                contato_id = int(input("Digite o ID do contato a remover: ")) ## Solicita o ID do contato a remover e tenta converter para inteiro.
                remover_contato_por_id(contato_id) ## Chama a função para remover o contato por ID.
            except ValueError: ## Captura o erro se a entrada não for um número inteiro.
                print("ID inválido. Por favor, digite um número inteiro.") ## Imprime uma mensagem de erro para ID inválido.
        elif opcao == "5": ## Verifica se a opção escolhida é "5" (Sair).
            print("Saindo da agenda. Até mais!") ## Imprime uma mensagem de despedida.
            break ## Sai do loop do menu.
        else: ## Se a opção for inválida.
            print("Opção inválida! Por favor, escolha uma opção de 1 a 5.") ## Imprime uma mensagem de opção inválida.


# Este bloco garante que o menu só será executado quando o script for rodado diretamente ## Comentário explicativo do bloco if __name__ == "__main__".
if __name__ == "__main__": ## Verifica se o script está sendo executado como programa principal.
    menu() ## Chama a função menu para iniciar a aplicação.
