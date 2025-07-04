import sqlite3

class Backend:
    @staticmethod
    def initDB():
        conexao = sqlite3.connect("nomes.db")
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)
        conexao.commit()
        conexao.close()

    @staticmethod
    def salvar_nome(nome):
        conexao = sqlite3.connect("nomes.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome,))
        conexao.commit()
        conexao.close()
        
