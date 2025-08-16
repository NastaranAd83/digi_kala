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

   


        

        


            