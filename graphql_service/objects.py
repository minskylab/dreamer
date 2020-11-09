import graphene

class Activity(graphene.ObjectType):
    id = graphene.ID()
    activity_type = graphene.String()
    nombre_cliente =  graphene.String()
    observaciones =  graphene.String()
    foto_fachada = graphene.String()
    foto_cintillo = graphene.String()
