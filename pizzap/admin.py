from django.contrib import admin

from .models import Order, Pizza, Customer, Ingredient


class IngredientInline(admin.TabularInline):
    model = Pizza.ingredients.through
    extra = 0


class PizzaAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    fields = ['name', 'price', 'photo', 'thumbnail']
    readonly_fields = ['thumbnail']


# Register your models here.
admin.site.register(Order)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Customer)
admin.site.register(Ingredient)
