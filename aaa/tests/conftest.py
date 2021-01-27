import pytest
from django.contrib.auth import get_user_model
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.utils.testing import graphql_query
from graphene_django.views import GraphQLView

from aaa.schema import schema


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


@pytest.fixture
def create_user():
    get_user_model().objects.create_user("username", "user@mail.com", "password")


urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
