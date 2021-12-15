from django.contrib.auth.models import User
from django.db import models
from thumbnailerist.thumbnail import Photo


class Pizza(Photo):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return f'{self.name} (Price : {self.price})'

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=100)
    item_ordered = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    total_amount = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
