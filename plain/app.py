import sys

from django.conf import settings
from django.conf.urls import url
from django.core.management import execute_from_command_line

from schema import schema


settings.configure(
    DEBUG=True,
    SECRET_KEY='A-random-secret-key!',
    ROOT_URLCONF=sys.modules[__name__],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
        },
    ],
    INSTALLED_APPS=('graphene_django',),
)

# Need to import after settings are loaded
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^graphql', GraphQLView.as_view(schema=schema, graphiql=True)),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
