from typing import List, Any
from copy import deepcopy

class Stack:
    # Classe genérica, pode receber qualquer tipo de dado
    def __init__(self) -> None:
        self.__data: List[Any] = []
        self.__index = 0
    
    # Representa o método append de uma lista 
    def append(self, item: Any) -> None:
        self.__data.append(item)
    
    # Representa o método pop de uma lista sem a passagem 
    # do parâmetro de índice
    def pop(self) -> Any:
        if not self.__data:
            return
        
        return self.__data.pop()

    # Exibe o último elemento adicionado à Stack
    def peek(self) -> Any:
        if not self.__data:
            return

        return self.__data[-1]
    
    # Método de representação de dados
    def __repr__(self) -> str:
        return str(self.__data)

    # Método para iteração com for
    def __iter__(self):
        self.__index = len(self.__data)
        return self
    
    # Método para iteração com for (next item)
    def __next__(self):
        if self.__index == 0:
            raise StopIteration()

        self.__index -= 1
        return self.__data[self.__index]
    
    # Método para iteração com while
    def __bool__(self):
        return bool(self.__data)