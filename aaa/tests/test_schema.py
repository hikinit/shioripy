import json

import pytest

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.urls("aaa.tests.conftest"),
]


@pytest.mark.usefixtures("create_user")
def test_mutation_login(client_query):
    response = client_query(
        """
        mutation {
            tokenAuth(username: "username", password: "password"){
                token
            }
        }
        """
    )
    response = json.loads(response.content)

    assert "errors" not in response
    assert "token" in response["data"]["tokenAuth"]


def test_mutation_registration(client_query):
    response = client_query(
        """
        mutation {
            register(
                username: "user",
                password1: "SecretKey2",
                password2: "SecretKey2"
            ) {
                token
                success
                errors
            }
        }
        """,
    )
    response = json.loads(response.content)
    response = response["data"]["register"]

    assert response["errors"] is None
    assert response["success"] is True


@pytest.mark.usefixtures("create_user")
def test_mutation_verify_token(client_query):
    login_response = client_query(
        """
        mutation {
            tokenAuth(username: "username", password: "password"){
                token
            }
        }
        """
    )
    login_response = json.loads(login_response.content)
    token = login_response["data"]["tokenAuth"]["token"]

    response = client_query(
        """
        mutation VerifyToken($token: String!){
            verifyToken(token: $token){
                success,
                errors,
                payload
            }
        }
        """,
        variables={"token": token},
    )

    response = json.loads(response.content)
    response = response["data"]["verifyToken"]

    assert response["errors"] is None
    assert response["success"] is True
