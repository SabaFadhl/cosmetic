from django.db import models
from makeup.models import Products
from django.contrib.auth.models import User


class favorite(models.Model):
    """
    this class model for post link is connect post id with user
    """
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['product', 'user']]


    def __str__(self):
        return self.user.username + ' ' +str(self.product.name)

