# Projeto Agenda de Contatos

## Objetivo do Projeto

O principal propósito deste projeto é oferecer uma **ferramenta de gerenciamento de contatos robusta, porém de fácil utilização**, operando inteiramente através de uma **interface de linha de comando (CLI)**. A aplicação foi concebida para simplificar a organização de informações de contato, sejam elas de natureza pessoal ou profissional.

Através de um conjunto intuitivo de comandos, os usuários podem:

* **Adicionar Contatos:** Cadastrar novas entradas, incluindo detalhes como nome, telefone, CPF e endereço, garantindo que suas informações estejam sempre acessíveis.
* **Listar Contatos:** Visualizar uma lista completa de todos os contatos salvos, apresentada de forma clara e organizada para facilitar a consulta.
* **Buscar Contatos:** Realizar buscas rápidas e eficientes por contatos específicos, utilizando partes do nome para encontrar rapidamente a informação desejada.
* **Remover Contatos:** Excluir entradas indesejadas da agenda de forma permanente, mantendo a base de dados limpa e atualizada.

A persistência e segurança dos dados são garantidas pelo uso de um **banco de dados SQLite local**. Esta escolha proporciona um armazenamento eficiente e autônomo, eliminando a necessidade de configurações complexas de servidor e tornando a aplicação totalmente portátil. O programa foi projetado para ser intuitivo, com um menu interativo que guia o usuário pelas opções disponíveis, tornando a experiência de gerenciamento de contatos simples e direta.

---

## Como Executar o Projeto

Para configurar e executar este programa em seu ambiente local, siga os passos detalhados abaixo:

### Pré-requisitos

Certifique-se de ter o **Python 3** (versão 3.6 ou superior é recomendada) instalado em sua máquina. Você pode baixar a versão mais recente e estável diretamente do site oficial: [python.org](https://www.python.org/downloads/).

### Instalação

1.  **Obtenha os Arquivos do Projeto:**
    * Se o projeto estiver hospedado em um repositório Git (como GitHub, GitLab, Bitbucket), clone-o para o seu computador usando o comando:

        ```bash
        git clone <URL_DO_REPOSITORIO>
        ```
    * Caso contrário, baixe os arquivos do projeto (geralmente um arquivo `.zip`) e extraia-os para uma pasta de sua preferência em seu sistema.

2.  **Navegue até o Diretório do Projeto:**
    Abra o seu terminal ou prompt de comando e use o comando `cd` (change directory) para navegar até a pasta onde você salvou os arquivos do projeto. Por exemplo:

    ```bash
    cd /caminho/para/seu/projeto/agenda_de_contatos
    ```
    Substitua `/caminho/para/seu/projeto/agenda_de_contatos` pelo caminho real da pasta em seu computador.

### Execução

Com o terminal posicionado no diretório raiz do projeto, execute o script principal da agenda. Geralmente, o nome do arquivo principal é `agenda.py` ou `main.py`.

```bash
python agenda.py

**Desenvolvido por:** [Antonio Victor Monteiro de Souza]
**Disciplina/Curso:** [Programação Senai]
**Data:** [Concluido 03/07/2025]