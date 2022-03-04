import graphene

from graphene_django import DjangoObjectType
from graphql import GraphQLError

from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link
        fields = '__all__'


class Query(graphene.ObjectType):
    links = graphene.List(LinkType, url=graphene.String())

    def resolve_links(root, info, url=None, **kwargs):
        if not url:
            link = Link.objects.all()
        else:
            link = Link.objects.find_url(url)
        return link


class CreateLink(graphene.Mutation):
    url = graphene.Field(LinkType)

    class Arguments:
        received_url = graphene.String()

    def mutate(self, info, received_url):
        validate = URLValidator()

        try:
            validate(received_url)
        except ValidationError as error:
            raise GraphQLError(f'invalid url: {error}')
        url = Link(
            received_url=received_url,
            short_url=BaseUserManager().make_random_password()
            ).save()

        return CreateLink(url=url)


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
