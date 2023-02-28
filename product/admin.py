from django.contrib import admin

from .models import Category, Catalog, Basket, Sale, Delivery, Organization, Invoice

# Добавление модели на главную страницу интерфейса администратора
admin.site.register(Category)
admin.site.register(Catalog)
admin.site.register(Basket)
admin.site.register(Sale)
admin.site.register(Delivery)
admin.site.register(Organization)
admin.site.register(Invoice)
