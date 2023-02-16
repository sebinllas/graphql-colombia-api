import strawberry
import typing

from models.City import City

strawberry.type 
class TouristAtrraction:
    id: int
    name: str 
    description: typing.Optional[str]
    images: typing.Optional[typing.List[str]]
    latitude: typing.Optional[str]
    longitude: typing.Optional[str]
    city: typing.Optional[City]