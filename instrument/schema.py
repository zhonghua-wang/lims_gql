from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters
from instrument import models


class DepartmentNode(DjangoObjectType):
    class Meta:
        model = models.Department
        interfaces = (relay.Node,)


class InstrumentNode(DjangoObjectType):
    class Meta:
        model = models.Instrument
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, id, context, info):
        try:
            return cls._meta.model.objects.get(pk=id)
        except cls._meta.model.DoesNotExist:
            return None


class InstrumentFilter(django_filters.FilterSet):
    department = django_filters.UUIDFilter

    class Meta:
        model = models.Instrument
        exclude = ['image']


class ReservationNode(DjangoObjectType):
    class Meta:
        model = models.Reservation
        interfaces = (relay.Node,)


class ReservationFilter(django_filters.FilterSet):
    user = django_filters.UUIDFilter
    reserved = django_filters.TimeRangeFilter

    class Meta:
        model = models.Reservation
        exclude = []


class Query(AbstractType):
    instrument = relay.Node.Field(InstrumentNode)
    all_instruments = DjangoFilterConnectionField(
        InstrumentNode,
        filterset_class=InstrumentFilter
    )
    department = relay.Node.Field(DepartmentNode)
    all_departments = DjangoFilterConnectionField(DepartmentNode)
