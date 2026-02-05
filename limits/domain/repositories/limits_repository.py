# Connect with database
import os
import mysql.connector

class LimitDb:

    def __init__(self):

        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)),
        )
        
        self.cursor = self.conn.cursor(dictionary=True)
    
    def create_limit(self, wallet_id, daily_limit, monthy_limit):

        sql = """
            INSERT INTO limits (wallet_id, daily_limit, daily_limit_used, monthy_limit, monthy_limit_used)
            VALUES (%s, %s, %s, %s, %s)
        """

        self.cursor.execute(sql, (wallet_id, daily_limit, 0.0, monthy_limit, 0.0))
        self.conn.commit()

    def get_limit(self, wallet_id):

        sql = """
            SELECT
                *
            FROM    
                limits
            WHERE   
                wallet_id = %s
        """

        self.cursor.execute(sql, (wallet_id,))
        return self.cursor.fetchone()
    
    def list_limits(self):

        sql = """
            SELECT
                *
            FROM    
                limits
        """

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_limits(self, wallet_id, daily_limit, daily_limit_used, monthy_limit, monthy_limit_used):

        sql = """
                UPDATE 
                    wallet
                SET 
                    daily_limit = %s
                    daily_limit_used = %s
                    monthy_limit = %s
                    monthy_limit_used = %s
                WHERE
                    wallet_id = %s
                """
        
        self.cursor.execute(sql, (wallet_id, daily_limit, daily_limit_used, monthy_limit, monthy_limit_used))
        self.conn.commit()

    def delete_limits(self, wallet_id):

        sql = """
            DELETE FROM
                limits
            WHERE
                wallet_id = %s
            """
        
        self.cursor.execute(sql, (wallet_id,))
        self.conn.commit()

    def close(self):

        self.cursor.close()
        self.conn.close()