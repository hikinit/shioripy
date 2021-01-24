import graphene
from graphene_django import DjangoObjectType

from series.models import Series


class SeriesType(DjangoObjectType):
    class Meta:
        model = Series
        fields = "__all__"
        convert_choices_to_enum = False

    origin = graphene.String(resolver=lambda series, info: series.origin.name)


class Query(graphene.ObjectType):
    series = graphene.List(SeriesType)

    @staticmethod
    def resolve_series(root, info):
        return Series.objects.all()
