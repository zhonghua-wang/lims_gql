import graphene
from graphene_django.debug import DjangoDebug
import instrument.schema
import core.schema


class Query(instrument.schema.Query, core.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
