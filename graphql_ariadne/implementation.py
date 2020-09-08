from persistence.dreams import save_dream
from entities import DreamDraft
from ariadne import load_schema_from_path, QueryType, MutationType, make_executable_schema


query = QueryType()
mutation = MutationType()


@query.field("health")
def resolve_health(_, info) -> str:
    request = info.context["request"]
    print(request)
    return "ok"


@mutation.field("registerNewDream")
def resolve_register(_, info, dream, date, dreamer) -> str:
    print(dream, date, type(dreamer))

    dreamer = dict(
        id=dreamer["id"] if "id" in dreamer else "",
        name=dreamer["name"],
        age=dreamer["age"] if "age" in dreamer else -1
    )

    obj: DreamDraft = DreamDraft(dreamer, dream, date)
    dream_id = save_dream(obj)
    return dream_id


type_defs = load_schema_from_path("./graphql_ariadne/schema.graphql")

schema = make_executable_schema(type_defs, query,  mutation)
