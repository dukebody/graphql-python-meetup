from django.contrib.auth.models import User
from django.db.models import Avg

import graphene
from graphene_django import DjangoObjectType
from graphene_django.fields import DjangoListField
from .models import Product, Review


class ProductType(DjangoObjectType):
    stars = graphene.Int()

    class Meta:
        model = Product

    def resolve_review(self, args, context, info):
        return self.review_set.all()

    def resolve_stars(self, args, context, info):
        return self.review_set.aggregate(Avg('stars'))['stars__avg']


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.AbstractType):
    product = graphene.Field(ProductType, id=graphene.Int())
    products = DjangoListField(ProductType)
    user = graphene.Field(UserType, id=graphene.Int())
    users = DjangoListField(UserType)

    def resolve_product(self, args, context, info):
        return Product.objects.get(id=args['id'])

    def resolve_products(self, args, context, info):
        return Product.objects.all()

    def resolve_user(self, args, context, info):
        return User.objects.get(id=args['id'])

    def resolve_users(self, args, context, info):
        return User.objects.all()
