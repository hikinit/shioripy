import pytest
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.utils.testing import graphql_query
from graphene_django.views import GraphQLView

from series.models import MediaType, Series
from series.schema import schema


@pytest.fixture
def series():
    return Series(
        title="Strike Witches",
        media=MediaType.CARTOON,
    )


@pytest.fixture
def dummy_series():
    Series.objects.create(
        title="Strike Witches",
        media=MediaType.CARTOON,
        origin="JP",
    )


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
