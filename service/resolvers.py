from graphql_ariadne import schema
from persistence.dreams import save_dream
from entities import DreamDraft

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


@app.route('/register-dream', methods=["POST"])
async def register_dream(request):
    data = await request.json()
    obj: DreamDraft = DreamDraft(data['dreamer'], data['dream'], data['date'])
    dream_id = save_dream(obj)
    res = JSONResponse({"id": dream_id})
    return res
