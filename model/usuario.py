from database.conexao import conectar

def cadastro(login:str, senha:str):
    try:
        conexao, cursor = conectar()

        cursor.execute("""INSERT INTO cadastro (usuario, senha)
                        VALUES (%s, %s)""", [login, senha])
        conexao.commit()

        conexao.close()

        return True
    except Exception as erro:
        print (erro)
        return False