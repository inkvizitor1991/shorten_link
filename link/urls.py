from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from link.views import (
    root, index, add_link,
    prepare_link, show_links,
    search_about_links
)


urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('add_link/', add_link, name='add_link'),
    path('prepare_link/', prepare_link, name='prepare_link'),
    path('show_links/', show_links, name='show_links'),
    path('search_about_links/', search_about_links, name='search_about_links'),
    path('prepare_link/<str:short_url>/', root, name='root'),
    path('', index, name='index'),

]

