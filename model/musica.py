from database.conexao import conectar

def recuperar_msc():
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica;")
    
    dic_msc = cursor.fetchall()

    conexao.close()

    return dic_msc

def salvarmusic(cantor:str, duracao:str, nome:str, url_imagem:str, nome_genero:str) -> bool:
    """
    O adicionar música vai adicionar as músicas no seu banco de dados.
    """
    try:
        conexao, cursor = conectar()

        cursor.execute("""INSERT INTO musica (cantor, duracao, nome, url_imagem, nome_genero)
                    VALUES (%s, %s, %s, %s, %s)""",
                    [cantor, duracao, nome, url_imagem, nome_genero])

        conexao.commit()

        conexao.close()

        return True
    except Exception as erro:
        print (erro)
        return False
    
def deletar(codigo:int):

    conexao, cursor = conectar()

    cursor.execute("DELETE FROM musica WHERE codigo = %s",[codigo])
    
    conexao.commit()

    conexao.close()

def ativar_msc(codigo:int, status:bool):

    conexao, cursor = conectar()

    cursor.execute("""UPDATE musica 
                   SET ativo = %s
                   WHERE codigo = %s""", [status, codigo])
    
    conexao.commit()

    conexao.close()

    

   