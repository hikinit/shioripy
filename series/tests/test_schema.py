import json

import pytest

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.urls("series.tests.conftest"),
]


@pytest.mark.usefixtures("dummy_series")
def test_query_series(client_query):
    response = client_query("{ series { title media origin } }")
    response = json.loads(response.content)

    assert response["data"]["series"][0] == {
        "title": "Strike Witches",
        "media": "Cartoon",
        "origin": "Japan",
    }


def test_mutation_create_series_unauthenticated(client_query):
    response = client_query(
        """
        mutation {
            createSeries(
                title: "Strike Witches",
                media: CARTOON
                origin: "jp"
            ) {
                series {
                    title
                    origin
                    mediaL10n
                }
            }
        }
    """
    )
    response = json.loads(response.content)

    assert "errors" in response


def test_mutation_create_series_authenticated(authenticated_client_query):
    response = authenticated_client_query(
        """
        mutation {
            createSeries(
                title: "Strike Witches",
                media: CARTOON
                origin: "jp"
            ) {
                series {
                    title
                    origin
                    mediaL10n
                }
            }
        }
    """
    )
    response = json.loads(response.content)

    assert "errors" not in response
    assert response["data"]["createSeries"]["series"] == {
        "title": "Strike Witches",
        "origin": "Japan",
        "mediaL10n": "Anime",
    }
