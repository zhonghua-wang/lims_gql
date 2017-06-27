from core import models
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters


class UserNode(DjangoObjectType):
    class Meta:
        model = models.User
        interfaces = (relay.Node,)


class Query(AbstractType):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
