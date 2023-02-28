from django.shortcuts import render, redirect

# Класс HttpResponse из пакета django.http, который позволяет отправить текстовое содержимое.
from django.http import HttpResponse, HttpResponseNotFound
# Конструктор принимает один обязательный аргумент – путь для перенаправления. Это может быть полный URL (например, 'https://www.yahoo.com/search/') или абсолютный путь без домена (например, '/search/').
from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

# Подключение моделей
from .models import Category, Catalog, ViewCatalog, Basket, Sale, Delivery, Organization, Invoice, ViewSale
# Подключение форм
from .forms import CategoryForm, CatalogForm, SignUpForm, DeliveryForm, OrganizationForm, InvoiceForm

from django.db.models import Sum

from django.db import models

import datetime

import sys

#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth import login as auth_login

from django.db.models.query import QuerySet

# Create your views here.
# Групповые ограничения
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='403')

# Стартовая страница 
def index(request):
    catalog = ViewCatalog.objects.all().order_by('?')[0:4]
    reviews = ViewSale.objects.exclude(rating=None).order_by('?')[0:4]
    return render(request, "index.html", {"catalog": catalog, "reviews": reviews})    

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def category_index(request):
    category = Category.objects.all().order_by('title')
    return render(request, "category/index.html", {"category": category,})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def category_create(request):
    try:
        if request.method == "POST":
            category = Category()
            category.title = request.POST.get("title")
            categoryform = CategoryForm(request.POST)
            if categoryform.is_valid():
                category.save()
                return HttpResponseRedirect(reverse('category_index'))
            else:
                return render(request, "category/create.html", {"form": categoryform})
        else:        
            categoryform = CategoryForm()
            return render(request, "category/create.html", {"form": categoryform})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Category.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Category.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def category_edit(request, id):
    try:
        category = Category.objects.get(id=id)
        if request.method == "POST":
            category.title = request.POST.get("title")
            categoryform = CategoryForm(request.POST)
            if categoryform.is_valid():
                category.save()
                return HttpResponseRedirect(reverse('category_index'))
            else:
                return render(request, "category/edit.html", {"form": categoryform})
        else:
            # Загрузка начальных данных
            categoryform = CategoryForm(initial={'title': category.title, })
            return render(request, "category/edit.html", {"form": categoryform})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def category_delete(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return HttpResponseRedirect(reverse('category_index'))
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
def category_read(request, id):
    try:
        category = Category.objects.get(id=id) 
        return render(request, "category/read.html", {"category": category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def catalog_index(request, invoice_id):
    #catalog = Catalog.objects.all().order_by('title')
    invoice = Invoice.objects.get(id=invoice_id)
    catalog = Catalog.objects.filter(invoice_id=invoice_id).order_by('title')
    return render(request, "catalog/index.html", {"catalog": catalog, "invoice": invoice, "invoice_id": invoice_id})
    
# Список для просмотра и отправки в корзину
#@login_required
def catalog_list(request):
    try:
        # Только доступный товар
        catalog = ViewCatalog.objects.filter(available__gt=0).order_by('title')
        # Подчситать количество товара в корзине доступны записи только текущего пользователя
        # Текущий пользователь
        _user_id = request.user.id
        basket_count = Basket.objects.filter(user_id=_user_id).count()
        #print(basket_count)        
        if request.method == "POST":
            # Выделить id товара
            catalog_id = request.POST.dict().get("catalog_id")
            #print("catalog_id ", catalog_id)
            price = request.POST.dict().get("price")
            #print("price ", price)
            user = request.POST.dict().get("user")
            #print("user ", user)
            # Отправить товар в корзину
            basket = Basket()
            basket.catalog_id = catalog_id
            basket.price = float(int(price.replace(",00","")))
            #basket.price = price
            basket.user_id = user
            basket.save()
            message = _('Item added to basket')
            basket_count = Basket.objects.filter(user_id=_user_id).count()
            return render(request, "catalog/list.html", {"catalog": catalog, "mess": message, "basket_count": basket_count })
        else:
            return render(request, "catalog/list.html", {"catalog": catalog, "basket_count": basket_count })
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)
    
# Корзина
@login_required
def basket(request):
    try:
        # Текущий пользователь
        _user_id = request.user.id
        # Доступны записи только текущего пользователя
        basket = Basket.objects.filter(user_id=_user_id).order_by('basketday')
        # Подсчитать стоимость товара в корзине
        basket_total = 0
        for b in basket:
            basket_total = basket_total + b.price*b.quantity
        #print(total)        
        # Если это подтверждение какого-либо действия
        if request.method == "POST":        
            # Увеличение или уменьшение количества товара в корзине
            if ('btn_plus' in request.POST) or ('btn_minus' in request.POST):
                # Выделить id записи в корзине и количество товара       
                basket_id = request.POST.dict().get("basket_id")
                quantity = request.POST.dict().get("quantity")
                # Найти запись в корзине
                basket = Basket.objects.get(id=basket_id)
                # Изменить запись в корзине
                if 'btn_plus' in request.POST:
                    basket.quantity = basket.quantity + 1
                if 'btn_minus' in request.POST:
                    if basket.quantity > 1:
                        basket.quantity = basket.quantity - 1
                # Сохранить
                basket.save()
                # Доступны записи только текущего пользователя
                basket = Basket.objects.filter(user_id=_user_id).order_by('basketday')
                # Подсчитать стоимость товара в корзине
                basket_total = 0
                for b in basket:
                    basket_total = basket_total + b.price*b.quantity
                return render(request, "catalog/basket.html", {"basket": basket, "basket_total": basket_total})
            # Приобретение, если нажата кнопка Buy
            if 'buy' in request.POST:
                # Перебрать всю корзину отправить ее в продажи!
                for b in basket:
                    # Добавить в продажи
                    sale = Sale()
                    sale.catalog_id = b.catalog_id
                    sale.price = b.price
                    sale.quantity = b.quantity
                    sale.user_id = b.user_id
                    sale.details = ""
                    #print("Сохранено")
                    sale.save()
                # Очистить корзину
                #print("Корзина очищена")
                basket.delete()
                # Перейти к совершенным покупкам
                return HttpResponseRedirect(reverse("buy"))
        else:
            return render(request, "catalog/basket.html", {"basket": basket, "basket_total": basket_total})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление из корзины
@login_required
def basket_delete(request, id):
    try:
        basket = Basket.objects.get(id=id)                
        basket.delete()
        # Текущий пользователь
        _user_id = request.user.id
        # Доступны записи только текущего пользователя
        basket = Basket.objects.filter(user_id=_user_id).order_by('basketday')
        # Подсчитать стоимость товара в корзине
        basket_total = 0
        for b in basket:
            basket_total = basket_total + b.price*b.quantity    
        return render(request, "catalog/basket.html", {"basket": basket, "basket_total": basket_total})
    except Catalog.DoesNotExist:
        return HttpResponseNotFound("<h2>Basket not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)
    
# Список приобретения + Оставление отзыва
@login_required
def buy(request):
    try:
        # Текущий пользователь
        _user_id = request.user.id
        print(_user_id)
        # Доступны записи только текущего пользователя
        sale = Sale.objects.filter(user_id=_user_id).order_by('saleday')    
        # Если это подтверждение какого-либо действия
        if request.method == "POST":
            # Отправить отзыв, если нажата кнопка Review
            if 'review' in request.POST:
                # Выделить id записи в таблице sale        
                sale_id = request.POST.dict().get("sale_id")
                review = Sale.objects.get(id=sale_id) 
                review.rating = request.POST.dict().get("rating")
                review.details = request.POST.dict().get("rating_details")
                #print(sale_id)
                #print(review.rating)
                #print(review.details)
                review.save()            
                return render(request, "catalog/buy.html", {"sale": sale})
        else:
            return render(request, "catalog/buy.html", {"sale": sale})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def catalog_create(request, invoice_id):
    try:
        if request.method == "POST":
            catalog = Catalog()
            catalog.invoice_id = invoice_id
            catalog.category = Category.objects.filter(id=request.POST.get("category")).first()
            catalog.code = request.POST.get("code")
            catalog.title = request.POST.get("title")
            catalog.info = request.POST.get("info")
            catalog.details = request.POST.get("details")        
            catalog.price = request.POST.get("price")
            catalog.quantity = request.POST.get("quantity")
            if 'photo' in request.FILES:                
                catalog.photo = request.FILES['photo']
            catalogform = CatalogForm(request.POST)
            if catalogform.is_valid():
                catalog.save()
                return HttpResponseRedirect(reverse('catalog_index', args=(invoice_id,)))
            else:
                return render(request, "catalog/create.html", {"form": catalogform})
        else:        
            catalogform = CatalogForm()
            return render(request, "catalog/create.html", {"form": catalogform, "invoice_id": invoice_id})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Catalog.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Catalog.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def catalog_edit(request, id, invoice_id):
    try:
        catalog = Catalog.objects.get(id=id) 
        if request.method == "POST":
            catalog.category = Category.objects.filter(id=request.POST.get("category")).first()
            catalog.code = request.POST.get("code")
            catalog.title = request.POST.get("title")
            catalog.info = request.POST.get("info")
            catalog.details = request.POST.get("details")        
            catalog.price = request.POST.get("price")
            catalog.quantity = request.POST.get("quantity")
            if 'photo' in request.FILES:
                catalog.photo = request.FILES['photo']
            catalogform = CatalogForm(request.POST)
            if catalogform.is_valid():
                catalog.save()
                return HttpResponseRedirect(reverse('catalog_index', args=(invoice_id,)))
            else:
                return render(request, "catalog/edit.html", {"form": catalogform, "invoice_id": invoice_id})            
        else:
            # Загрузка начальных данных
            catalogform = CatalogForm(initial={'code': catalog.code, 'category': catalog.category, 'title': catalog.title, 'info': catalog.info, 'details': catalog.details, 'price': catalog.price, 'quantity': catalog.quantity, 'photo': catalog.photo, })
            #print('->',catalog.photo )
            return render(request, "catalog/edit.html", {"form": catalogform, "invoice_id": invoice_id})
    except Catalog.DoesNotExist:
        return HttpResponseNotFound("<h2>Catalog not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def catalog_delete(request, id, invoice_id):
    try:
        catalog = Catalog.objects.get(id=id)
        catalog.delete()
        return HttpResponseRedirect(reverse('catalog_index', args=(invoice_id,)))
    except Catalog.DoesNotExist:
        return HttpResponseNotFound("<h2>Catalog not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы с информацией о товаре для менеджера.
@login_required
@group_required("Managers")
def catalog_read(request, id, invoice_id):
    try:
        catalog = Catalog.objects.get(id=id) 
        return render(request, "catalog/read.html", {"catalog": catalog, "invoice_id": invoice_id})
    except Catalog.DoesNotExist:
        return HttpResponseNotFound("<h2>Catalog not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы с информацией о товаре для клиента
#@login_required
def catalog_details(request, id):
    try:
        # Товар с каталога
        catalog = ViewCatalog.objects.get(id=id)
        # Отзывы на данный товар
        reviews = ViewSale.objects.filter(catalog_id=id).exclude(rating=None)
        return render(request, "catalog/details.html", {"catalog": catalog, "reviews": reviews,})
    except Catalog.DoesNotExist:
        return HttpResponseNotFound("<h2>Catalog not found</h2>")
    
# Список продаж с указанием последнего движения в доставке
@login_required
def delivery_list(request):    
    if request.user.groups.filter(name='Managers').exists():
        view_sale = ViewSale.objects.all().order_by('-saleday')        
    else:
        _user_id = request.user.id
        view_sale = ViewSale.objects.filter(user_id=_user_id).order_by('-saleday')        
    return render(request, "delivery/list.html", {"view_sale": view_sale})
    
# Список для изменения с кнопками создать, изменить, удалить для конкретной доставки
@login_required
def delivery_index(request, id):
    try:
        delivery = Delivery.objects.filter(sale_id=id)
        view_sale = ViewSale.objects.get(id=id)
        return render(request, "delivery/index.html", {"delivery": delivery, "view_sale": view_sale})
    except Delivery.DoesNotExist:
        return HttpResponseNotFound("<h2>Delivery not found</h2>")

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def delivery_create(request, sale_id):
    try:
        if request.method == "POST":
            delivery = Delivery()
            delivery.sale_id = sale_id
            delivery.deliveryday = request.POST.get("deliveryday")
            delivery.movement = request.POST.get("movement")
            delivery.details = request.POST.get("details")
            deliveryform = DeliveryForm(request.POST)
            if deliveryform.is_valid():
                delivery.save()
                return HttpResponseRedirect(reverse('delivery_index', args=(delivery.sale_id,)))
            else:
                return render(request, "delivery/create.html", {"form": deliveryform})
        else:
            deliveryform = DeliveryForm()
            return render(request, "delivery/create.html/", {"form": deliveryform, 'sale_id': sale_id,})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Delivery.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Delivery.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def delivery_edit(request, id):
    try:
        delivery = Delivery.objects.get(id=id) 
        if request.method == "POST":
            delivery.movement = request.POST.get("movement")
            delivery.details = request.POST.get("details")
            deliveryform = DeliveryForm(request.POST)
            if deliveryform.is_valid():
                delivery.save()
                return HttpResponseRedirect(reverse('delivery_index', args=(delivery.sale_id,)))
            else:
                return render(request, "delivery/edit.html", {"form": deliveryform})
        else:
            # Загрузка начальных данных
            deliveryform = DeliveryForm(initial={'sale': delivery.sale, 'deliveryday': delivery.deliveryday, 'movement': delivery.movement, 'details': delivery.details,})
            return render(request, "delivery/edit.html", {"form": deliveryform, 'sale_id': delivery.sale_id, })
    except Delivery.DoesNotExist:
        return HttpResponseNotFound("<h2>Delivery not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def delivery_delete(request, id):
    try:
        delivery = Delivery.objects.get(id=id)
        delivery.delete()
        return HttpResponseRedirect(reverse('delivery_index', args=(delivery.sale_id,)))
    except Delivery.DoesNotExist:
        return HttpResponseNotFound("<h2>Delivery not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
def delivery_read(request, id):
    try:
        delivery = Delivery.objects.get(id=id) 
        return render(request, "delivery/read.html", {"delivery": delivery, "sale_id": delivery.sale_id})
    except Catalog.DoesNotExist:
        return HttpResponseNotFound("<h2>Catalog not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)
   
# Отчеты
def report_index(request):
    catalog = ViewCatalog.objects.all().order_by('title')
    sale = ViewSale.objects.all().order_by('saleday')
    delivery = Delivery.objects.all().order_by('deliveryday')
    review = ViewSale.objects.all().order_by('category', 'title', 'saleday')
    return render(request, "report/index.html", {"catalog": catalog, "sale": sale, "delivery": delivery, "review": review })

# Контакты
def contact(request):
    return render(request, "contact.html")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def organization_index(request):
    organization = Organization.objects.all().order_by('title')
    return render(request, "organization/index.html", {"organization": organization})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def organization_create(request):
    try:    
        if request.method == "POST":
            organization = Organization()
            organization.title = request.POST.get("title")
            organization.address = request.POST.get("address")
            organization.phone = request.POST.get("phone")                
            organizationform = OrganizationForm(request.POST)
            if organizationform.is_valid():
                organization.save()
                return HttpResponseRedirect(reverse('organization_index'))
            else:
                return render(request, 'organization/create.html', {'form': organizationform})            
        else:        
            organizationform = OrganizationForm()
            return render(request, "organization/create.html", {"form": organizationform})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
@login_required
@group_required("Managers")
def organization_edit(request, id):
    try:
        organization = Organization.objects.get(id=id) 
        if request.method == "POST":
            organization.title = request.POST.get("title")
            organization.address = request.POST.get("address")
            organization.phone = request.POST.get("phone")
            organizationform = OrganizationForm(request.POST)
            if organizationform.is_valid():
                print(organization.phone)
                organization.save()
                return HttpResponseRedirect(reverse('organization_index'))
            else:
                print(0)
                return render(request, "organization/edit.html", {"form": organizationform}) 
        else:
            # Загрузка начальных данных
            organizationform = OrganizationForm(initial={'title': organization.title, 'address': organization.address, 'phone': organization.phone })
            return render(request, "organization/edit.html", {"form": organizationform})
    except Organization.DoesNotExist:
        return HttpResponseNotFound("<h2>Organization not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def organization_delete(request, id):
    try:
        organization = Organization.objects.get(id=id)
        organization.delete()
        return HttpResponseRedirect(reverse('organization_index'))
    except Organization.DoesNotExist:
        return HttpResponseNotFound("<h2>Organization not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
def organization_read(request, id):
    try:
        organization = Organization.objects.get(id=id) 
        return render(request, "organization/read.html", {"organization": organization})
    except Organization.DoesNotExist:
        return HttpResponseNotFound("<h2>Organization not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def invoice_index(request):
    invoice = Invoice.objects.all().order_by('datei')
    return render(request, "invoice/index.html", {"invoice": invoice})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def invoice_create(request):
    try:
        if request.method == "POST":
            invoice = Invoice()
            invoice.organization = Organization.objects.filter(id=request.POST.get("organization")).first()
            invoice.datei = request.POST.get("datei")
            invoice.numb = request.POST.get("numb")
            invoiceform = InvoiceForm(request.POST)
            if invoiceform.is_valid():
                invoice.save()
                return HttpResponseRedirect(reverse('invoice_index'))
            else:
                return render(request, "invoice/create.html", {"form": invoiceform})
        else:        
            invoiceform = InvoiceForm(initial={'datei': datetime.datetime.now().strftime('%Y-%m-%d'), })        
            return render(request, "invoice/create.html", {"form": invoiceform})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
@login_required
@group_required("Managers")
def invoice_edit(request, id):
    try:
        invoice = Invoice.objects.get(id=id) 
        if request.method == "POST":
            invoice.organization = Organization.objects.filter(id=request.POST.get("organization")).first()
            invoice.datei = request.POST.get("datei")
            invoice.numb = request.POST.get("numb")
            invoiceform = InvoiceForm(request.POST)
            if invoiceform.is_valid():
                invoice.save()
                return HttpResponseRedirect(reverse('invoice_index'))
            else:
                return render(request, "invoice/edit.html", {"form": invoiceform})
        else:
            # Загрузка начальных данных
            invoiceform = InvoiceForm(initial={'organization': invoice.organization, 'datei': invoice.datei.strftime('%Y-%m-%d'), 'numb': invoice.numb })
            return render(request, "invoice/edit.html", {"form": invoiceform})
    except Invoice.DoesNotExist:
        return HttpResponseNotFound("<h2>Invoice not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def invoice_delete(request, id):
    try:
        invoice = Invoice.objects.get(id=id)
        invoice.delete()
        return HttpResponseRedirect(reverse('invoice_index'))
    except Invoice.DoesNotExist:
        return HttpResponseNotFound("<h2>Invoice not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
def invoice_read(request, id):
    try:
        invoice = Invoice.objects.get(id=id) 
        return render(request, "invoice/read.html", {"invoice": invoice})
    except Invoice.DoesNotExist:
        return HttpResponseNotFound("<h2>Invoice not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)
    
# Регистрационная форма 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
            #return render(request, 'registration/register_done.html', {'new_user': user})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# Изменение данных пользователя
@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('index')
    #success_url = reverse_lazy('my_account')
    def get_object(self):
        return self.request.user

