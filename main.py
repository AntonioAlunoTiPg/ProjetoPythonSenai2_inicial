import tkinter as tk # Importa a biblioteca tkinter, usada para criar interfaces gráficas de usuário (GUIs).
from Gui import Gui # Importa a classe Gui do módulo Gui.py, que define a interface do usuário da aplicação.
from Backend import Backend # Importa a classe Backend do módulo Backend.py, que lida com a lógica de armazenamento de dados e outras operações de backend.

def main(): # Define a função principal onde a execução da aplicação começa.
    Backend.initDB() # Chama o método initDB da classe Backend para inicializar o banco de dados ou o sistema de armazenamento de dados.
    root = tk.Tk() # Cria a janela principal (raiz) da aplicação tkinter.
    app = Gui(root) # Cria uma instância da classe Gui, passando a janela raiz para seu construtor. Isso configura os elementos da interface do usuário.
    root.mainloop() # Inicia o loop de eventos do tkinter. Isso faz com que a janela apareça e permite que ela responda às interações do usuário até ser fechada.

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente (não importado como um módulo).
    main() # Se o script for executado diretamente, chama a função main para iniciar a aplicação.