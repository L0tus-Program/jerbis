import sqlite3




def inserir(titulo,data,hora,descricao):
    

    conn = sqlite3.connect('callendar.db')
    cursor = conn.cursor()

    # Inserir um evento no banco de dados
    cursor.execute("INSERT INTO Eventos (titulo, data, hora, descricao) VALUES (?, ?, ?, ?)", (titulo, data, hora, descricao))

    # Commit para salvar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()



def consultar():


    conn = sqlite3.connect('callendar.db')
    cursor = conn.cursor()

    # Consulta eventos em uma data específica
    cursor.execute("SELECT * FROM Eventos WHERE data = ?", ('2023-12-10',))
    eventos = cursor.fetchall()

    for evento in eventos:
        print(evento)

    # Fechar a conexão
    conn.close()




titulo = "Testando agora"
data = '2023-12-10'
hora = '18:00'
descricao = 'Fazendo um teste de calendario'


inserir(titulo,data,hora,descricao)


consultar()