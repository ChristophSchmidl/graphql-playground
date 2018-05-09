import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

from links.models import Link, Vote
from users.schema import UserType

class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    links = graphene.List(
        LinkType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int())

    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
        qs = Link.objects.all()

        # The value sent with the search parameter will be on the args variable
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(description__icontains=search)
            )
            qs = qs.filter(filter)

        if skip:
            qs = qs[skip::]

        if first:
            qa = qs[:first]

        return qs

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            # This Error produces the same output later on as a simple Exception
            raise GraphQLError('You must be logged to vote!')

        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)


'''
# 1
Defines a mutation class. Right after, you define the output of the mutation, 
the data the server can send back to the client. The output is defined field 
by field for learning purposes. On the next mutation you’ll define them as 
just one.
'''
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    '''
    # 2
    Defines the data you can send to the server, in this case, the links’ 
    url and description.
    '''
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    '''
    # 3
    The mutation method: it creates a link on the database using the data 
    sent by the user, through the url and description parameters. After, the 
    server returns the CreateLink class with the data just created. See how 
    this matches the parameters set on #1.

    '''
    def mutate(self, info, url, description):
        user = info.context.user or None

        link = Link(
            url=url,
            description=description,
            posted_by=user
        )
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by,
        )
'''
# 4
Creates a mutation class with a field to be resolved, which points to our mutation 
defined before.
'''
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()