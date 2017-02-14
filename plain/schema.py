import graphene

from data import data


class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()


class Review(graphene.ObjectType):
    id = graphene.Int()
    product = graphene.Field(lambda: Product)
    product_id = graphene.Int()
    user_id = graphene.Int()
    user = graphene.Field(User)
    stars = graphene.Int()
    title = graphene.String()
    body = graphene.String()

    def resolve_user(self, args, context, info):
        return User(**data['users'][self.user_id])

    def resolve_product(self, args, context, info):
        return Product(**data['products'][self.product_id])


class Product(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    detail = graphene.String()
    image = graphene.String()
    stars = graphene.Int()

    reviews = graphene.List(Review)

    def resolve_reviews(self, args, context, info):
        reviews = data['reviews'].values()
        reviews_data = filter(lambda rev: rev['product_id'] == self.id, reviews)
        return [Review(**rd) for rd in reviews_data]

    def resolve_stars(self, args, context, info):
        reviews = self.resolve_reviews(args, context, info)
        if reviews:
            return sum(review.stars for review in reviews) / len(reviews)
        else:
            return 0


class Query(graphene.ObjectType):
    products = graphene.List(Product)
    product = graphene.Field(Product, id=graphene.Int())
    users = graphene.List(User)
    user = graphene.Field(User, id=graphene.Int())

    # @graphene.resolve_only_args
    def resolve_products(self, args, context, info):
        products_data = data['products'].values()
        return [Product(**p_data) for p_data in products_data]

    def resolve_product(self, args, context, info):
        _id = args['id']
        p_data = data['products'][_id]
        return Product(**p_data)

    def resolve_users(self, args, context, info):
        users_data = data['users'].values()
        return [User(**u_data) for u_data in users_data]

    def resolve_user(self, args, context, info):
        u_data = data['users'][args['id']]
        return User(**u_data)


schema = graphene.Schema(query=Query)
