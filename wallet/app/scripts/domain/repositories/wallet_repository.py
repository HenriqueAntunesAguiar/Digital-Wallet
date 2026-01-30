
# Connect with database
import os
import mysql.connector

class WalletDb:

    def __init__(self):

        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)),
        )
        
        self.cursor = self.conn.cursor(dictionary=True)
    
    def create_wallet(self, wallet_id, balance):

        sql = """
            INSERT INTO wallet (wallet_id, balance)
            VALUES (%s, %s)
        """

        self.cursor.execute(sql, (wallet_id, balance))
        self.conn.commit()

    def get_wallet(self, wallet_id):

        sql = """
            SELECT
                *
            FROM    
                wallet
            WHERE   
                wallet_id = %s
        """

        self.cursor.execute(sql, (wallet_id,))
        return self.cursor.fetchone()
    
    def list_wallets(self):

        sql = """
            SELECT
                *
            FROM    
                wallet
        """

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_wallet(self, wallet_id, new_balance):

        sql = """
                UPDATE 
                    wallet
                SET 
                    balance = %s
                WHERE
                    wallet_id = %s
                """
        
        self.cursor.execute(sql, (new_balance, wallet_id))
        self.conn.commit()

    def delete_wallet(self, wallet_id):

        sql = """
            DELETE FROM
                wallet
            WHERE
                wallet_id = %s
            """
        
        self.cursor.execute(sql, (wallet_id,))
        self.conn.commit()

    def close(self):

        self.cursor.close()
        self.conn.close()