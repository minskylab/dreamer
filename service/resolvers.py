from graphql_ariadne import schema
from entities import Case
from extraction import scrapper

# Using Starlette

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

# from starlette.graphql import GraphQLApp
from ariadne.asgi import GraphQL


routes = [
    Route('/graphql', GraphQL(schema=schema, debug=True))
]

app = Starlette(debug=True, routes=routes)



@app.route('/process-case', methods=["GET"])
async def process_case(request):
    data = await request.json()
    obj: Case =  scrapper(data['code'])
    obj: Pcase= processcase(Case)
    
    return Pcase