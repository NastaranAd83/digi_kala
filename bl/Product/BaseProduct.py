
from dataclasses import dataclass


@dataclass
class Product:
    brand: str
    model: str
    name: str
    price: float
    os: str

    # def __init__(self, brand , model ,name , price, os ) -> None:
    #     self._brand = brand
    #     self._model = model
    #     self._name = name
    #     self._price = price
    #     self._os = os

    #     @property
    #     def color(self):
    #         return self.__color

    #     @color.setter
    #     def color(self , color ) -> list:
            
    #         self.__color = color 
    #         return self.__color


        



    

