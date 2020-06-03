import mysql.connector


class Database:
    def __init__(self, host, user, password, database_name):
        self.connection = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            database=database_name,
            password=password
        )

    def insert(self, sql, data):
        cursor = self.connection.cursor()
        cursor.execute(sql, data)
        self.connection.commit()
        cursor.close()
        self.connection.close()


db = Database("127.0.0.1", "root", "", "yobba")
