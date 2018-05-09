import graphene
import graphql_jwt

import links.schema
import users.schema
import links.schema_relay


class Query(
    users.schema.Query,
    links.schema.Query,
    links.schema_relay.RelayQuery,
    graphene.ObjectType):
    pass

class Mutation(
    users.schema.Mutation,
    links.schema.Mutation,
    links.schema_relay.RelayMutation,
    graphene.ObjectType):

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)