



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


    def read_records(self, table_name,username:str=None):
        # SELECT * FROM factors where username = "io"
        if table_name == "factors":
            sql = "SELECT * FROM {} WHERE username = %s".format(table_name)
            self.cursor.execute(sql,(username,))
            for row in self.cursor.fetchall():
                print(row)

        else:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            for row in self.cursor.fetchall():
                print(row)

    def update_record(self, list_product):

        tables = ["laptop", "cellphone"]
        ids = list_product
        for table in tables:
            placeholders = ", ".join(["%s"] * len(ids))
            sql = f"UPDATE {table} SET stock = stock - 1 WHERE id IN ({placeholders})"
            self.cursor.execute(sql, ids)
            self.conn.commit()
            # print("✅ رکورد ویرایش شد.")

    def delete_record(self):
        tables = ["laptop", "cellphone"]
       
        for table in tables :
            sql = f"DELETE FROM {table} WHERE stock = 0"
            self.cursor.execute(sql)
            self.conn.commit()
        # print("✅ رکورد حذف شد.")

    def close(self):
        self.cursor.close()
        self.conn.close()

    def return_id_name(self,list_product:list):

        num = 0 
        tables = ["laptop", "cellphone"]
        ids = list_product
        data =[]

        for table in tables:
            placeholders = ", ".join(["%s"] * len(ids))
            sql = f"SELECT id, name, price FROM {table} WHERE id IN ({placeholders})"
            self.cursor.execute(sql, ids)
            rows = self.cursor.fetchall()
            for row in rows:
                print(f"{table}: id = {row[0]}, name = {row[1]}, price = {row[2]}")
                dict_data = {"table_name":table,"name":row[1],"price":row[2]}
                data.append(dict_data)
                num = row[2] + num
        return num ,data

    def add_factors(self , table_name , data_list):
        
        columns = ', '.join(data_list[0].keys())

        for item in data_list:
            placeholders = ', '.join(['%s'] * len(item))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(sql, tuple(item.values()))
            self.conn.commit()

    

        
   

    







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

        
        
        