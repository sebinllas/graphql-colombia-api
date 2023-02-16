import strawberry
import typing
from datetime import date

from models.City import City

@strawberry.type 
class President:
    id: int
    image: typing.Optional[str]
    name: str
    lastname: str
    period_start_date: date
    period_end_date: date
    political_party: typing.Optional[str]
    deascription: typing.Optional[str]
    city: typing.Optional[City]