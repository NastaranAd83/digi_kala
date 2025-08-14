



import mysql.connector


class DatabaseManager:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()


    def insert_row(self ,table_name, values : list):
    
        pass


    def read_records(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        for row in self.cursor.fetchall():
            print(row)

    def update_record(self, table_name, set_clause, condition, values):
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("✅ رکورد ویرایش شد.")

    def delete_record(self, table_name, condition, values):
        sql = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("✅ رکورد حذف شد.")

    def close(self):
        self.cursor.close()
        self.conn.close()

    def return_id(self,table_name):
        self.cursor.execute(f"SELECT id FROM {table_name}")
        for row in self.cursor.fetchall():
            print(row)






# class SqlHelper:

    

# try:
#     host = '127.0.0.1'
#     connection = mysql.connector.connect(
#         host=host,
#         database='MySql',
#         user='root',
#         password=''
#     )

#     if connection.is_connected():
#         db_info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_info)

#         cursor = connection.cursor()
#         cursor.execute("select database()")  # حذف دو نقطه اضافی
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except mysql.connector.Error as e:  # تصحیح خطای except
#     print("Error while connecting to MySQL", e)

# finally:
#     if 'connection' in locals() and connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

        
        
        