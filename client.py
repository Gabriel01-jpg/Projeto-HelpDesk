import sqlite3
from conexao import Conexao

class register_Client:

    def register(self,nomeCliente,sobrenomeCliente,CPF,telefoneCliente,enderecoCliente,emailCliente):
        try:
            conn = Conexao()
            conexao = conn.connect()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Clientes (nomeCliente,sobrenomeCliente,CPF,telefoneCliente,enderecoCliente,emailCliente) VALUES (?,?,?,?,?,?)'
            cursor.execute(sql,(nomeCliente,sobrenomeCliente,CPF,telefoneCliente,enderecoCliente,emailCliente))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de departamentos: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def consult(self):
        conn = Conexao()
        conexao = conn.connect()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM Clientes').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset


    def consult_details(self, idCliente):  
        conn = Conexao()
        conexao = conn.connect()
        cursor = conexao.cursor()


        try:
            resultset =  cursor.execute('SELECT * FROM Clientes WHERE idCliente = ?', (idCliente,)).fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        

        cursor.close()
        conexao.close()
        return resultset


    def consult_last_id(self):
        conn = Conexao()
        conexao = conn.connect()
        cursor = conexao.cursor()

        try:
            resultset = cursor.execute('SELECT MAX(idCliente) FROM Clientes').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]


    def update(self,idCliente,nomeCliente,sobrenomeCliente,CPF,telefoneCliente,enderecoCliente,emailCliente):
        try:
            conn = Conexao()
            conexao = conn.connect()
            cursor = conexao.cursor()

            sql = 'UPDATE Clientes SET nomeCliente = ?, sobrenomeCliente = ?, CPF = ?, telefoneCliente = ?,enderecoCliente = ?,emailCliente = ? WHERE idCliente = (?)'
            cursor.execute(sql,(idCliente,nomeCliente,sobrenomeCliente,CPF,telefoneCliente,enderecoCliente,emailCliente))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na Atualização de Clientes: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de Integridade: {}".format(e))
            return False


    def delete(self,idCliente):
        try:
            conn = Conexao()
            conexao = conn.connect()
            cursor = conexao.cursor()

            sql = 'DELETE FROM Clientes WHERE idCliente = (?)'
            cursor.execute(sql,[idCliente])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de departamentos: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False