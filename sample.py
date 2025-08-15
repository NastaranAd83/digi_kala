
# # # # # # import re

# # # # from tabulate import tabulate


# # # # # # # # class Person:
# # # # # # # #     def __init__(self, name , family , phone) -> None:

# # # # # # # #         self.name = name 
# # # # # # # #         self.family = family
# # # # # # # #         self.phone = phone 


# # # # # # # #     @property
# # # # # # # #     def name(self):
# # # # # # # #         return self.__name

# # # # # # # #     @name.setter
# # # # # # # #     def name(self , name ):
        
# # # # # # # #         error=[]
# # # # # # # #         if not name:
# # # # # # # #             error.append("empty name")

# # # # # # # #         elif not isinstance(name, str):
# # # # # # # #             raise TypeError(f"invalid type")

# # # # # # # #         else :
# # # # # # # #             self.__name = name 
# # # # # # # #             return self.__name



# # # # # # # # pe = Person('',"kk",'09129593968')



# # # # # # # res = re.match(r"^09\d{9}$","09129593968")
# # # # # # # print (res)



# # # # # # class Person:
# # # # # #     def __init__(self, name , family , phone) -> None:

# # # # # #         super().__init__(**kwargs)
# # # # # #         self.name = name 
# # # # # #         self.family = family
# # # # # #         self.phone = phone 



# # # # # # class UserPass(Person):

# # # # # #     def __init__(self, name :str , family:str , phone:str , username:str  , password:str ) -> None:
# # # # # #         super().__init__(name, family, phone)
# # # # # #         self.username = username
# # # # # #         self.password = password




# # # # # # class SignUp(UserPass):

# # # # # #     def __init__(self, username:str, password:str ):
# # # # # #         UserPass.__init__(self, username, password)
    
# # # # # #     # def request_for_admin(self):

# # # # # #     #     list_request = []
# # # # # #     #     list_request.append(f"this user {self.name} , {self.family} wants to sign up (username :{self.username}) ")

# # # # # #     #     FilaManagering.save_data(list_data=list_request,file_path=r"file\request_login.json")

# # # # # #     #     print("your request It has sent to the admin")
    


# # # # # data = {
# # # # #     {
# # # # #         "product": "Laptop",
# # # # #         "price": 1200,
# # # # #         "in_stock": True
# # # # #     }
# # # # #     {
# # # # #         "product": "Laptop",
# # # # #         "price": 1200,
# # # # #         "in_stock": True
# # # # #     }

# # # # # }
data =[ {"name" : "nstrn" , "family": "adib"} , {"name" : " nrn" , "family": "op"},{"name" : " mn" , "family": "iu"}]

# # # # # def mono(): 
# # # # #         errors = []
# # # # #         target_data = next(( item for item in data if item["name"] == "nstrn"), None)

# # # # #         if target_data:
# # # # #             errors.append(f"name exists!!")

# # # # #         return errors , target_data

# # # # # error , data1 = mono()

# # # # # print(error)
# # # # # print(data1)

# # #     # گرفتن کلیدها از اولین دیکشنری
# # # headers = list(data[0].keys())

# # # # چاپ هدر
# # # print(" , ".join(headers))

# # # # چاپ ردیف‌ها
# # # for row in data:
# # #     print(" , ".join(str(row.get(h, "")) for h in headers))


# # # # print(tabulate(data, headers="keys"))





# # try:
    
# #     # host='127.0.0.1'
# #     # host='localhost'
# #     connection = mysql.connector.connect(host='127.0.0.1',
# #                                          database='PythonClass',
# #                                          user='root',
# #                                          password='')
# #     if connection.is_connected():
# #         db_Info = connection.get_server_info()
# #         print("Connected to MySQL Server version ", db_Info)
        
# #         cursor = connection.cursor()
        
# #         cursor.execute("select database();")
        
        
# #         record = cursor.fetchone()
# #         print("You're connected to database: ", record)

# # except Error as e:
# #     print("Error while connecting to MySQL", e)
    
# # finally:
# #     if connection.is_connected():
# #         cursor.close()
# #         connection.close()
# #         print("MySQL connection is closed")
        
import mysql.connector

# try:
#     host = '127.8.0.1'
#     # یا host = 'localhost'
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


class DatabaseManager:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()


    # def insert_row(self ,table_name, values : list):
    

    #     if len(values) != 7 :
    #         raise ValueError("all of record should be valid")

    
    #     sql = f"INSERT INTO {table_name} {values[0], values[0], values[0], values[0], values[0], values[0], values[0]} VALUES {%s, %s, %s, %s, %s, %s, %s}"
        
    #     self.cursor.execute(sql, values)

        
    #     self.conn.commit()

    #     # بستن اتصال
    #     self.cursor.close()
    #     self.conn.close()
    #     print("Done!")


    def read_records(self, table_name):
       
        self.cursor.execute(f"SELECT * FROM {table_name} where stock!=0")
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

    def return_id_name(self,list_product:list):
        tables = ["laptop", "cellphone"]
        ids = list_product
        num = 0
        for table in tables:
            
            placeholders = ", ".join(["%s"] * len(ids))
            sql = f"SELECT id, name , price FROM `{table}` WHERE id IN ({placeholders})"
            self.cursor.execute(sql, ids)
            rows = self.cursor.fetchall()
            for row in rows:
                print(f"{table}: id={row[0]}, name={row[1]}, price = {row[2]}")
                num = row[2] + num

        return num 

    def add_factors(self , table_name , data_list):
        
        columns = ', '.join(data_list[0].keys())

        for item in data_list:
            placeholders = ', '.join(['%s'] * len(item))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(sql, tuple(item.values()))
            self.conn.commit()
# f = []
# db = DatabaseManager(host="127.0.0.1",user="root",password="",database="mysql_helper")
# db.read_records("cellphone")
# db.read_records("laptop")
# f = [db.read_records("cellphone")]




db = DatabaseManager(host="127.0.0.1",user="root",password="",database="mysql_helper")
db.read_records("cellphone")
data = [ {"name":"nstrn","price" :0},{"name1":"nono","price" :12},{"name":"nono2","price" :120}]

target_data = next(( item for item in data if item["name"] == "nstrn"), None)

# print(target_data)

headers = list(target_data.keys())
print("   ,   ".join(headers))
print("--"*47)
print("   ,   ".join(str(target_data.get(h, "")) for h in headers)) 
        

db.add_factors("factors",data)
# db.add_factors("factors",data)

# db.read_records("laptop")


# num =db.return_id_name([1,2,3])
# print (num)


# while(True):

#         print ("\n which one do you want ?")
#         print ("please enter the id of the ")

#         id_ = input("id : ")

#         try :
#             id_ = int (id_)

#         except:

#             db1= DatabaseManager(host="127.0.0.1",user="root",password="",database="mysql_helper")
#             print("invalid value for id ")
            


#         else:
#             break


