import json

import pytest

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.urls("aaa.tests.conftest"),
]


@pytest.mark.usefixtures("create_user")
def test_mutation_create_series(client_query):
    variables = {"username": "username", "password": "password"}

    response = client_query(
        """
        mutation TokenAuth($username: String!, $password: String!){
            tokenAuth(username: $username, password: $password){
                token
            }
        }
        """,
        variables=variables,
    )
    response = json.loads(response.content)

    assert "errors" not in response
    assert "token" in response["data"]["tokenAuth"]
