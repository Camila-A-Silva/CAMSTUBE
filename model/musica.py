from database.conexao import conectar

def recuperar_msc():
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")
    
    dic_msc = cursor.fetchall()

    conexao.close()

    return dic_msc