#########################################
#Feito por Davi Fabiano e Nafftaly Lopes#
#########################################

import sqlite3
from conexao import Conexao

class Produtos():

    def cadastrar(self, nome, descricao):
        try:
            conn = Conexao()
            conexao = conn.connect()
            cursor = conexao.cursor()

            sql = 'INSERT INTO Produtos(nomeProduto, descricaoProduto) values(?, ?)'
            cursor.execute(sql,(nome, descricao))

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as err:
            print(f'Falha ao inserir valores no banco! \nErro: {err}')
        except sqlite3.IntegrityError as err:
            print(f'Falha ao inserir valores no banco! \nErro: {err}')
        except sqlite3.Error as err:
            print(f'Falha ao inserir valores no banco! \nErro: {err}')


    def consultar(self):
        conn = Conexao()
        conexao = conn.connect()
        cursor = conexao.cursor()
        try:
            resultset = cursor.execute('SELECT * FROM Produtos').fetchall()
        except sqlite3.Error as err:
            print(f'Falha ao buscar produtos no banco! \nErro: {err}')
        
        cursor.close()
        conexao.close()
        return resultset

    def consultarDetalhes(self, idProduto):
        conn = Conexao()
        conexao = conn.connect()
        cursor = conexao.cursor()

        sql = "SELECT * FROM Produtos WHERE idProduto = ?"

        try:
            resultset = cursor.execute(sql, [idProduto]).fetchone()
        except sqlite3.Error as err:
            print(f'Falha ao buscar produto no banco! \nErro: {err}')

        cursor.close()
        conexao.close()
        return resultset
        
    def consultarUltimoID(self):
        conn = Conexao()
        conexao = conn.connect()
        cursor = conexao.cursor()

        try:
            resultset = cursor.execute('SELECT MAX(idProduto) FROM Produtos').fetchone()
        except sqlite3.Error as err:
            print(f"Falha ao buscar produto no banco! \nErro: {err}")


        
        
        cursor.close()
        conexao.close()
        return resultset[0]

    def update(self, idProduto, nome, descricao = 'Null'):
        try:
            conn = Conexao()
            conexao = conn.connect()
            cursor = conexao.cursor()

            sql = 'UPDATE produtos SET nomeProduto = ?, descricaoProduto = ? WHERE idProduto = (?)'
            cursor.execute(sql,(nome, descricao, idProduto))
        
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de departamentos: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

    def excluir(self, idProduto):
        try:
            conn = Conexao()
            conexao = conn.connect()
            cursor = conexao.cursor()

            sql = 'DELETE FROM Produtos WHERE idProduto = (?)'
            cursor.execute(sql, [idProduto])

            conexao.commit()
            cursor.close()
            conexao.close()
            return True
        except sqlite3.OperationalError as err:
            print(f"Erro na exclusão de produto: {err}")
            return False
        except sqlite3.IntegrityError as err:
            print(f"Erro de integridade: {err}")
            return False
