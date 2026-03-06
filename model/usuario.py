from database.conexao import conectar

def cadastro(login:str, senha:str):
    try:
        conexao, cursor = conectar()

        cursor.execute("""INSERT INTO cadastro (login, senha)
                        VALUES (%s, %s)""", [login, senha])
        conexao.commit()

        conexao.close()

        return True
    except Exception as erro:
        print (erro)
        return False
    

def verificar_usuario(login:str, senha:str) -> list:
        """Função que verifica se o usuário está cadastrado, se estiver cadastrado retorna os dados do usuário,
        se não estiver retorno None"""
    
        conexao, cursor = conectar()

        cursor.execute("""SELECT login, senha FROM cadastro
                       WHERE login = %s and senha = %s""",[login, senha])

        usuario = cursor.fetchone()

        conexao.close()

        return usuario