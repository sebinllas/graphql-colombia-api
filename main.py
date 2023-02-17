from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
import typing

from data_fetching import get_departments
from mappers.department_mapper import department_mapper
from models.Deparment import Deparment

@strawberry.type
class Query:

    @strawberry.field(description="Returns a list of departments")
    def departments(self) -> typing.List[Deparment]:
        return map(lambda d: department_mapper(d), get_departments())
    
    @strawberry.field(description="Returns a department by id")
    def department(self, id: int) -> Deparment:
        return department_mapper(get_departments()[id])
    


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
