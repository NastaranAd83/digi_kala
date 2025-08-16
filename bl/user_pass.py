from bl.person import Person
from dataclasses import dataclass
import re

@dataclass
class UserPass():

   
    @staticmethod
    def check_validation (password:str) -> list:

        error_list = []

        if len(password) < 8 :
            error_list.append("len less than 8")

        if not re.search(r"[a-z]", password):
            error_list.append("It doesn't have lower letter")
    
        if not re.search(r"[A-Z]", password):
            error_list.append("It doesn't have upper letter")
    
        if not re.search(r"\d", password):
            error_list.append("It doesn't have number")
    
        if not re.search(r"[@$!%*?&]", password):
            error_list.append("It doesn't have especific character")

        return error_list



    
        
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self , username ):

        self.__username = username
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self , password ) :
        # error_list = self.check_validation(password)
        # if error_list:
        #     print("weak password")
        #     for error in error_list:
        #         print(error)

        # else:
        #     print("strong password")
        #     self.__password = password
        #     return self.__password
        self.__password = password
        return self.__password

