 
from os import system
from time import sleep
from typing import Any, Callable
from dal.textmanager import FilaManagering


class Utility:

    @staticmethod
    def sarching(key:str, value:str)->  tuple[list[str] , dict | None]:

        

        data = FilaManagering.load_data(r"file\user_pass.json")
        target_data = next(( item for item in data if item[key] == value), None)

        if target_data:

           return [f"{key} already exists!"], target_data

        else:
            return [] , None



    @staticmethod
    def printing(dict_data:dict) -> None :

        headers = list(dict_data.keys())
        print("   ,   ".join(headers))
        print("--"*48)
        print("   ,   ".join(str(dict_data.get(h, "")) for h in headers)) 

    @staticmethod
    def get_valid_input(prompt : str , validators :  list[Callable[[str], list[str] | tuple[str | None, Any] | str | None]]) -> str:
        while True:

            system("cls")
            value = input(prompt)
            errors = []

            for validator in validators:
                result = validator(value)
    
                if isinstance(result, list):
                    errors.extend(result)
                
                elif isinstance(result, tuple):
                    err, _ = result
                    if err:  
                        errors.append(err)

                elif isinstance(result, str):
                    errors.append(result)

            if not errors:
                return value

            for err in errors:
                print(err)
            sleep(2)

    
    @staticmethod
    def get_fixed_input(prompt : str , correct_value : str, error_message : str) -> str :
        
        while True:
            
            system("cls")
            value = input(prompt)
            if value == correct_value:
                return value
            print(error_message)
            sleep(2)
            

    @staticmethod
    def validate_number(value: str, allow_float: bool = True,
                        min_value: float | None = None) -> tuple[list[str], float | None]:
        errors = []
        number = None

        try:
            number = float(value) if allow_float else int(value)
        except ValueError:
            errors.append(" Invalid number format.")
            return errors, None

        if min_value is not None and number < min_value:
            errors.append(f"Value must be greater than or equal to {min_value}.")


        return errors, number


                        
            

       

        

    