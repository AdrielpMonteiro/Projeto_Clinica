import sqlite3


def conexao_db():
    try:
        conexao = sqlite3.connect("clinica.db")
        cursor = conexao.cursor()
        print("conexão estabelecida com sucesso")
        return conexao,cursor
    except sqlite3.Error as erro:
        print("Falha ao se conectar ao banco de dados",erro)
        return None,None

##Criando banco de dados com exceção e tratamento try
def criando_db():
    try:
        conexao,cursor=conexao_db()
        if not conexao or not cursor:
            return

        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        senha TEXT NOT NULL,
                        nascimento TEXT NOT NULL
                    )
                ''')
        conexao.commit()
        print("Tabela 'usuarios' ,criada com sucesso")
        return conexao,cursor
    except sqlite3.Error as erro:
        print("Errou ao criar a tabela",erro)
        return None,None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        print("Conexão encerrada ")

criando_db()

