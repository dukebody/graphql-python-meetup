from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    detail = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    stars = models.IntegerField()
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.product_id, self.title)
