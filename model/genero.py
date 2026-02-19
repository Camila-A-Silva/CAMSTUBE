from database.conexao import conectar

def recuperar_gen():
    conexao, cursor = conectar()

    cursor.execute("SELECT nome_genero, icone, cor FROM genero;")

    # Recuperando os dados 
    dic_gen = cursor.fetchall()
    
    # Fechando a conexão
    conexao.close()

    return dic_gen