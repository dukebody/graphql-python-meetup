from django.conf.urls import url
from django.contrib import admin

import graphene
from graphene_django.views import GraphQLView

from djapp.schema import Query as DJAppQuery


class Query(DJAppQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql/', GraphQLView.as_view(schema=schema, graphiql=True)),
]
