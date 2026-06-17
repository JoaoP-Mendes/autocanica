import pymysql.connections

conexao = pymysql.connections.Connection(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "autocanica"
)

cursor = conexao.cursor()
