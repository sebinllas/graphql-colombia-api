import typing
from typing import Optional
import strawberry

from models.Deparment import Deparment
from models.President import President
from models.TouristAtrraction import TouristAtrraction

@strawberry.type
class City:
    id: int
    name: str
    description: Optional[str]
    surface: Optional[float]
    population: Optional[float]
    postal_code: Optional[str]
    department_id: int
    department: Deparment
    tourist_atractions: typing.List[TouristAtrraction]
    presidents: typing.List[President]