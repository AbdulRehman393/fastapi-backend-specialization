from typing import Any

# FastAPI uses Python type hints to understand what data an API expects
# and what type of data it returns.




name: str = "Abdul Rehman"
marks: int = 95
weight: float = 72.5

value: int | float = 12

class City:
    def __init__(self, name, location):
        self.name = name
        self.location = location


# List type hinting
digits: list[int] = [1, 2, 3, 4, 5]

# Tuple type hinting
# hinting that the given tuple contains multiples integers
multpile_3: tuple[int, ...] = (3, 6, 9, 12, 15)

hampshire = City("hampshire", 273829)



# The main usage of tuple is that we have some fixed values, here we are not only
# hinting the datatype of each element, we are also hinting on the lenght of the 
# tuple, which would be only two elements.
# This is also telling thee first element should be a City object and second elemnet 
# should be float
city_temp: tuple[City, float] = (hampshire, 38.6)

# Dictionary type hinting
shipment: dict[str, str | Any] = {
    "id": 27361,
    "weight": 62.3,
    "content":"wooden table",
     "status": "in transit"

     }



def root(num:  float, exp: float | None = .5) -> float:
    return pow(num, .5)

root_num = root(25)

print(root_num)


# To get warning when we provide a differet type of value than expextedm we can use 
# Mypy Type Checker