from dataclasses import dataclass, field
import re


@dataclass
class Person:
    name: str
    family: str
    phone: str
    username : str 
    password : str
    account_balance: float = field(default=0.0)




    @staticmethod
    def validation(value: str, is_phone: bool = False) -> list[str]:
        
        errors = []
        if not value:
            errors.append("empty value")

        elif not is_phone:
            if not value.isalpha():
                errors.append("invalid character")

        else:
            if not re.match(r"^(\+98|0)?9\d{9}$", value):
                errors.append("invalid phone number")

        return errors


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

   


        

        


            