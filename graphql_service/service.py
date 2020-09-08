
from typing import Dict
import graphene
import random
from persistence.dreams import save_dream
from entities import DreamDraft, DreamerDraft


class GQLDreamerDraft(graphene.InputObjectType):
    id = graphene.String()
    name = graphene.String()
    age = graphene.Int()


class RegisterNewDream(graphene.Mutation):
    id = graphene.String()

    class Arguments:
        dream = graphene.String(required=True)
        date = graphene.String(required=True)
        dreamer = GQLDreamerDraft()

    def mutate(root, info, dream: str, date: str, dreamer: GQLDreamerDraft):
        print(dream, date, dreamer)
        dreamer = dict(
            id=dreamer.id,
            name=dreamer.name,
            age=dreamer.age
        )
        obj: DreamDraft = DreamDraft(dreamer, dream, date)
        dream_id = save_dream(obj)

        return RegisterNewDream(id=dream_id)


class Query(graphene.ObjectType):
    health = graphene.String()

    def resolve_health(self, info):
        if random.random() > 0.5:
            return "ok"
        else:
            return "failed"


class Mutations(graphene.ObjectType):
    register_new_dream = RegisterNewDream.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
