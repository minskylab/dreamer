import graphene


class Dreamer(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()


class Dream(graphene.ObjectType):
    id = graphene.ID()
    dream = graphene.String()
    date = graphene.String()
    registered_at = graphene.String()
    dreamer = graphene.Field(Dreamer)
