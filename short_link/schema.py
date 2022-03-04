import graphene

import link.schema
import link.schema

class Query(link.schema.Query, graphene.ObjectType):
    pass

class Mutation(link.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)