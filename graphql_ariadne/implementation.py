from persistence.dreams import save_dream
from entities import DreamDraft
from ariadne import load_schema_from_path, QueryType, MutationType, make_executable_schema
from extraction.scrapper import scrapper

query = QueryType()
mutation = MutationType()


@query.field("live")
def resolve_live(_, info) -> str:
    //como se verifica que este vivo el proceso, el simple hecho de responder ok podria esta bien
    request = info.context["request"]
    print(request)
    return "ok"


@query.field("process")
def resolve_process(_, info) -> str:
    //nose que poner aca, todo esta en service/resolvers.py
    request = info.context["request"]
    print(request)
    return "ok"




type_defs = load_schema_from_path("./graphql_ariadne/schema.graphql")

schema = make_executable_schema(type_defs, query,  mutation)
