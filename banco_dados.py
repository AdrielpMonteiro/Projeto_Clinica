from base64 import encode

import sqlite3


def conexao_db():
    try:
        conexao = sqlite3.connect("clinica.db")
        cursor = conexao.cursor()
        print("conexão estabelecida com sucesso")
        return conexao, cursor
    except sqlite3.Error as erro:
        print("Falha ao se conectar ao banco de dados", erro)
        return None, None


##Criando banco de dados com exceção e tratamento try
def criando_db():
    try:
        conexao, cursor = conexao_db()
        if not conexao or not cursor:
            return

        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        senha TEXT NOT NULL,
                        nascimento TEXT NOT NULL,
                        email TEXT NOT NULL

                    )
                ''')

        cursor.execute('''
                           CREATE TABLE IF NOT EXISTS profissionais(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               nome TEXT NOT NULL,
                               senha TEXT NOT NULL,
                               crf TEXT NOT NULL,
                               email TEXT NOT NULL,
                               especialidade TEXT NOT NULL

                           )
                       ''')

        conexao.commit()
        print("Tabelas 'usuarios' ,'profissionais ,criadas com sucesso")
        return conexao, cursor
    except sqlite3.Error as erro:
        print("Errou ao criar a tabela", erro)
        return None, None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        print("Conexão encerrada ")


def cadastrar_usuario(nome, senha, nascimento, email):
    try:
        conexao, cursor = conexao_db()
        if not conexao or not cursor:
            return False

        cursor.execute('''
                     INSERT INTO usuarios (nome, senha, nascimento, email )
                    VALUES (?, ?, ?, ? )  ''', (nome, senha, nascimento, email))

        conexao.commit()
        return True
    except sqlite3.Error as erro:
        print("Erro ao cadastrar usuario", erro)
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def cadastrar_profissional(nome, senha, email, crf, especialidade):
    try:
        conexao, cursor = conexao_db()
        if not conexao or not cursor:
            return False

        cursor.execute('''
                    INSERT INTO profissionais (nome,senha,crf,email,especialidade)
                    VALUES (?, ?, ?, ?, ?)  ''', (nome, senha, crf, email, especialidade))

        conexao.commit()
        return True
    except sqlite3.Error as erro:
        print("Erro ao cadastrar profissional")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def verificar_login(nome, senha):
    try:
        conexao, cursor = conexao_db()
        if not conexao or not cursor:
            return False

        cursor.execute('SELECT senha FROM usuarios WHERE nome = ?', (nome,))
        resultado = cursor.fetchone()

        if resultado:
            senha_db = resultado[0]

            if senha == senha_db:
                print("Senha verificada com sucesso")
                return True

        return False
    except sqlite3.Error as erro:
        print("Erro ao verificar login ", erro)
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def deletar_usuario(id_usuario):
    try:
        conexao, cursor = conexao_db()
        if not conexao or not cursor:
            return False

        cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_usuario,))
        conexao.commit()
        print(f"Usuário com ID {id_usuario} deletado com sucesso!")
        return True
    except sqlite3.Error as erro:
        print("Erro ao deletar usuário", erro)
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def listar_usuario():
    try:
        conexao,cursor = conexao_db()
        if not conexao or not cursor:
            return []

        cursor.execute("SELECT id,nome,email,nascimento FROM usuarios")
        usuarios = cursor.fetchall()
        return usuarios
    except sqlite3.Error as erro:
        print("Erro ao listar  usuario",erro)
        return[]
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()






criando_db()