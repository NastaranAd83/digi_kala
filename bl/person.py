import re


class Person:
    def __init__(self, name , family , phone, account_balance=0) -> None:

        self.__name = name 
        self.__family = family
        self.__phone = phone 
        self.__account_balane = account_balance


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , name ) -> list:
    
            self.__name = name 
            return self.__name
            
    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self , family ):

        try :
            family = str(family)

        except ValueError :
            print ("invalid type")

        else :
            self.__family = family 
            return self.__family 

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self , phone ):
        
            self.__phone = phone 
            return self.__phone

    @property
    def balance(self):
        return self.__account_balane

    @balance.setter
    def balance(self , account_balane ):
        
            self.__account_balane = account_balane 
            return self.__account_balane


    # def get_error_lists(self):
    #     return self.__errors

    @staticmethod
    def validation(value,pattern:bool = False) -> list:

            errors = []

            if not value:
                errors.append("empty value")

            elif not pattern:
                if not value.isalpha():
                    errors.append("invalid character")

            elif pattern : 
                if not re.match(r"^(\+98|0)?9\d{9}$",value):
                    errors.append("inpropper phone number")


            return errors

        

        


            