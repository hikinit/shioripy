import pytest
from graphene import Schema
from graphene.test import Client
from series.models import MediaType, Series
from series.schema import Query

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    schema = Schema(query=Query)
    return Client(schema)


@pytest.fixture
def dummy_series():
    Series.objects.create(
        title="Strike Witches",
        media=MediaType.CARTOON,
        origin="JP",
    )


@pytest.mark.usefixtures("dummy_series")
def test_query_series(client):
    response = client.execute("{ series { title media origin } }")

    assert response["data"]["series"][0] == {
        "title": "Strike Witches",
        "media": "Cartoon",
        "origin": "Japan",
    }
