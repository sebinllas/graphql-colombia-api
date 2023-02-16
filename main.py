import strawberry
from typing import Optional
import typing
from data_fetching import get_departments

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from mappers.department_mapper import department_mapper

from models.Deparment import Deparment

departments: typing.List[dict] = get_departments()

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"
    
    @strawberry.type
    def departments(self) -> typing.List[Deparment]:
        return list(map(lambda d: department_mapper(d), departments))




schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")