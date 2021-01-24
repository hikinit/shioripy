import graphene
from graphene_django import DjangoObjectType

from series.models import MediaType, Series


class SeriesType(DjangoObjectType):
    class Meta:
        model = Series
        fields = "__all__"
        convert_choices_to_enum = False

    origin = graphene.String(resolver=lambda series, info: series.origin.name)
    media_l10n = graphene.String(
        resolver=lambda series, info: series.media_l10n,
    )


class CreateSeriesMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        media = graphene.Enum.from_enum(MediaType)(required=True)
        origin = graphene.String()

    series = graphene.Field(SeriesType)

    @staticmethod
    def mutate(root, info, title, media, origin):
        series = Series(
            title=title,
            media=media.value,
            origin=origin,
        )
        return CreateSeriesMutation(series=series)


class Query(graphene.ObjectType):
    series = graphene.List(SeriesType)

    @staticmethod
    def resolve_series(root, info):
        return Series.objects.all()


class Mutation(graphene.ObjectType):
    create_series = CreateSeriesMutation.Field()
