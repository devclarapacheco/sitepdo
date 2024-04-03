import psycopg2
from psycopg2 import Error

try:
    # Estabelece a conexão com o banco de dados PostgreSQL
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="localhost",
                                  port="5432",
                                  database="treino")

    cursor = connection.cursor()

    # Consulta SQL para recuperar os dados do Grupo1
    sql_query_grupo1 = "SELECT * FROM Grupo1"
    cursor.execute(sql_query_grupo1)
    records_grupo1 = cursor.fetchall()

    # Consulta SQL para recuperar os dados do Grupo2
    sql_query_grupo2 = "SELECT * FROM Grupo2"
    cursor.execute(sql_query_grupo2)
    records_grupo2 = cursor.fetchall()

    sql_query_ranking_quinzenal  = "SELECT * FROM  ranking_quinzenal "
    cursor.execute(sql_query_ranking_quinzenal )
    records_ranking_quinzenal  = cursor.fetchall()
    

    # Obtém os nomes das colunas da tabela Grupo1
    column_names_grupo1 = [desc[0] for desc in cursor.description]

    # Obtém os nomes das colunas da tabela Grupo2
    column_names_grupo2 = [desc[0] for desc in cursor.description]

    column_names_ranking_quinzenal  = [desc[0] for desc in cursor.description]

    # Escreve os dados em um arquivo HTML
    with open('index.html', 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Dados da Tabela</title>\n<link rel="stylesheet" type="text/css" href="site.css">\n</head>\n<body>\n')

        # Tabela para Grupo1
        f.write('<h2>Dados do Grupo1</h2>\n')
        f.write('<table border="1">\n<tr>')
        for col_name in column_names_grupo1:
            f.write(f'<th>{col_name}</th>')
        f.write('</tr>\n')
        for record in records_grupo1:
            f.write('<tr>')
            for value in record:
                f.write(f'<td>{value}</td>')
            f.write('</tr>\n')
        f.write('</table>\n')

        # Tabela para Grupo2
        f.write('<h2>Dados do Grupo2</h2>\n')
        f.write('<table border="1">\n<tr>')
        for col_name in column_names_grupo2:
            f.write(f'<th>{col_name}</th>')
        f.write('</tr>\n')
        for record in records_grupo2:
            f.write('<tr>')
            for value in record:
                f.write(f'<td>{value}</td>')
            f.write('</tr>\n')
        f.write('</table>\n')
        
        f.write('<h2>Ranking Quinzenal</h2>\n')
        f.write('<table border="1">\n<tr>')
        for col_name in column_names_ranking_quinzenal :
            f.write(f'<th>{col_name}</th>')
        f.write('</tr>\n')
        for record in records_ranking_quinzenal :
            f.write('<tr>')
            for value in record:
                f.write(f'<td>{value}</td>')
            f.write('</tr>\n')
        f.write('</table>\n')
       
        f.write('</body>\n</html>')

    print("Dados exportados com sucesso para 'index.html'.")

except (Exception, Error) as error:
    print("Erro ao conectar ao PostgreSQL:", error)

finally:
    # Fecha a conexão com o banco de dados
    if connection:
        cursor.close()
        connection.close()
        print("Conexão ao PostgreSQL encerrada.")
