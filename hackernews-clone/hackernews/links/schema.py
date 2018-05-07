import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


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
        link = Link(url=url, description=description)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )
'''
# 4
Creates a mutation class with a field to be resolved, which points to our mutation 
defined before.
'''
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()        