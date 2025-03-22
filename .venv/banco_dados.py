from base64 import encode

import sqlite3
import bcrypt ##USADO PARA SENHA SEGURA


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
        cursor.execute('''
                           CREATE TABLE IF NOT EXISTS administradores (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               nome TEXT NOT NULL,
                               senha TEXT NOT NULL,
                               nascimento TEXT NOT NULL,
                               email TEXT NOT NULL
                              
                           )
                       ''')
        conexao.commit()
        print("Tabelas 'usuarios' ,'profissionais , 'administradores',criadas com sucesso")
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

def cadastrar_usuario(nome , senha ,nascimento ,email):
    senha = senha.encode('utf-8')
    senha_hash = bcrypt.hashpw(senha,bcrypt.gensalt())
    try:
        conexao ,cursor = conexao_db()
        if not conexao or not cursor:
            return False

        cursor.execute('''
                     INSERT INTO usuarios (nome, senha, nascimento, email )
                    VALUES (?, ?, ?, ? )  ''',(nome,senha_hash,nascimento ,email ))

        conexao.commit()
        return True
    except sqlite3.Error as erro:
        print("Erro ao cadastrar usuario",erro)
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def cadastrar_profissional(nome, senha, email, crf, especialidade):
    senha = senha.encode('utf-8')
    senha_hash = bcrypt.hashpw(senha, bcrypt.gensalt())
    try:
        conexao, cursor = conexao_db()
        if not conexao or not cursor:
            return False

        cursor.execute('''
                    INSERT INTO profissionais (nome,senha,crf,email,especialidade)
                    VALUES (?, ?, ?, ?, ?)  ''', (nome, senha_hash, crf, email, especialidade))

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


def verificar_login(nome,senha):
    try:
        conexao,cursor = conexao_db()
        if not conexao or not cursor:
            return False

        cursor.execute('SELECT senha FROM usuarios WHERE nome = ?', (nome,))
        resultado = cursor.fetchone()

        if resultado:
            senha_hash = resultado[0]
            senha_hash = senha_hash.encode('utf-8')

            if bcrypt.checkpw(senha.encode('utf-8'),senha_hash):
                return True

        return False
    except sqlite3.Error as erro:
        print("Erro ao verificar login ",erro)
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

criando_db()



