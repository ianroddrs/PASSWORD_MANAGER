import sqlite3

# Criação banco de dados

def create_DB():
    conexao = sqlite3.connect('usuarios.db')
    c = conexao.cursor()
    c.execute('''CREATE TABLE user_cadastro (
            username text,
            email text,
            senha text
            )
        ''')
    conexao.commit()
    conexao.close()


def init(c, p):
    global components, page
    components = c
    page = p


def cadastrar_usuario(e):
        cadastro = {
            'username': components['username'].current.value,
            'email':  components['email'].current.value,
            'senha':  components['senha'].current.value
        }
        conexao = sqlite3.connect('usuarios.db')
        
        c = conexao.cursor()

        c.execute(" INSERT INTO user_cadastro VALUES(:username, :email, :senha)",
            {
                'username':cadastro['username'],
                'email':cadastro['email'],
                'senha':cadastro['senha']
            }
        )
        conexao.commit()
        conexao.close()