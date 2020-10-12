from django.contrib import admin
from .models import Product, Offer, Category, Customer, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'password')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity',
                    'price', 'date', 'status')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
