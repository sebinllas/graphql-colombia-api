import typing
import strawberry

#from models.City import City


@strawberry.type
class Deparment:
    id: int 
    name: str
    description: typing.Optional[str]
    #capital_city: typing.Optional[City]
    municipalities: typing.Optional[int]
    surface: float
    population: typing.Optional[int]
    phone_prefix: typing.Optional[str]
    #cities: typing.List[City]
