import MySQLdb, fabrica_conexao

class ClienteRepositorio():

    @staticmethod
    def listar_clientes():
        # Conexão com o banco:
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            # Criando cursor
            cursor = fabrica.cursor()
            cursor.execute("SELECT * FROM cliente;")
            print(cursor.fetchall())
        finally:
            fabrica.close()

    @staticmethod
    def inserir_cliente(cliente):
        # Conexão com o banco:
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            # Criando cursor
            cursor = fabrica.cursor()
            cursor.execute("INSERT INTO cliente(nome,idade) VALUES(%s,%s)", (cliente.nome, cliente.idade))
        finally:
            fabrica.close()

    @staticmethod
    def editar_cliente(id_cliente, cliente):
        # Conexão com o banco:
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            # Criando cursor
            cursor = fabrica.cursor()
            cursor.execute("UPDATE cliente SET nome=%(nome)s,idade=%(idade)s WHERE idcliente=%(id_cliente)s",
                       ({'nome': cliente.nome, 'idade': cliente.idade, 'id_cliente': id_cliente}))
        finally:
            fabrica.close()

    @staticmethod
    def remover_cliente(id_cliente):
        # Conexão com o banco:
        fabrica = fabrica_conexao.FabricaConexao.conectar()
        try:
            # Criando cursor
            cursor = fabrica.cursor()
            cursor.execute("DELETE FROM cliente WHERE idcliente=%s", (id_cliente,))
        finally:
            fabrica.close()