from typing import Optional
import typing
import strawberry

from models.City import City


@strawberry.type
class Deparment:
    id: int 
    name: str
    description: Optional[str]
    #capital_city: Optional[City]
    municipalities: Optional[int]
    surface: float
    population: Optional[int]
    phone_prefix: Optional[str]
    #cities: typing.List[City]
