"""
Django GraphQL Auth
Documentation: https://django-graphql-auth.readthedocs.io/en/latest/api
"""
import graphene
from graphql_auth import mutations
from graphql_auth.schema import MeQuery


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    update_account = mutations.UpdateAccount.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Query(MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
