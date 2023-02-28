from django.db import models
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from django.contrib.auth.models import User

# Модели отображают информацию о данных, с которыми вы работаете.
# Они содержат поля и поведение ваших данных.
# Обычно одна модель представляет одну таблицу в базе данных.
# Каждая модель это класс унаследованный от django.db.models.Model.
# Атрибут модели представляет поле в базе данных.
# Django предоставляет автоматически созданное API для доступа к данным

# choices (список выбора). Итератор (например, список или кортеж) 2-х элементных кортежей,
# определяющих варианты значений для поля.
# При определении, виджет формы использует select вместо стандартного текстового поля
# и ограничит значение поля указанными значениями.

# Категория товара
class Category(models.Model):
    # Читабельное имя поля (метка, label). Каждое поле, кроме ForeignKey, ManyToManyField и OneToOneField,
    # первым аргументом принимает необязательное читабельное название.
    # Если оно не указано, Django самостоятельно создаст его, используя название поля, заменяя подчеркивание на пробел.
    # null - Если True, Django сохранит пустое значение как NULL в базе данных. По умолчанию - False.
    # blank - Если True, поле не обязательно и может быть пустым. По умолчанию - False.
    # Это не то же что и null. null относится к базе данных, blank - к проверке данных.
    # Если поле содержит blank=True, форма позволит передать пустое значение.
    # При blank=False - поле обязательно.
    title = models.CharField(_('category_title'), max_length=128, unique=True)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'category'
    def __str__(self):
        # Вывод названияв тег SELECT 
        return "{}".format(self.title)

# Организации 
class Organization(models.Model):
    title = models.CharField(_('title_organization'), max_length=256)
    address = models.CharField(_('address'), max_length=128)
    phone = models.CharField(_('phone'), max_length=128)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'organization'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),            
        ]
        # Сортировка по умолчанию
        ordering = ['title']
    def __str__(self):
        # Вывод названия в тег SELECT 
        return "{}".format(self.title)
        # Override the save method of the model

# Приходные накладные 
class Invoice(models.Model):
    organization = models.ForeignKey(Organization, related_name='invoice_organization', on_delete=models.CASCADE)
    datei = models.DateTimeField(_('datei'))
    numb = models.IntegerField(_('numb'))     
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'invoice'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['datei']),            
        ]
        # Сортировка по умолчанию
        ordering = ['datei']
    def __str__(self):
        # Вывод названия в тег SELECT 
        return "{}".format(self.organization)
        # Override the save method of the model

# Каталог товаров
class Catalog(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='catalog_invoice', on_delete=models.CASCADE)
    code = models.CharField(_('code'), max_length=32, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='catalog_category', on_delete=models.CASCADE)
    title = models.CharField(_('catalog_title'), max_length=255)
    info = models.TextField(_('info'), blank=True, null=True)
    details = models.TextField(_('catalog_details'), blank=True, null=True)
    price = models.DecimalField(_('price'), max_digits=9, decimal_places=2)
    quantity = models.IntegerField(_('quantity'))
    photo = models.ImageField(_('photo'), upload_to='images/', blank=True, null=True)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'catalog'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),
        ]
        # Сортировка по умолчанию
        ordering = ['title']
    def __str__(self):
        # Вывод в тег SELECT 
        return "{} {} {}".format(self.category, self.title, self.price)
    """
    # Override the save method of the model
    def save(self):
        super().save()
        img = Image.open(self.photo.path) # Open image
        # resize image
        if img.height > 300 or img.width > 300:
            proportion_h_w = img.height/img.width  # Отношение высоты к ширине
            output_size = (int(proportion_h_w*300), 300)
            img.thumbnail(output_size) # Изменение размера
            img.save(self.photo.path) # Сохранение
    """
# Представление базы данных Каталог товаров (со средней оценкой)
#CREATE VIEW view_catalog AS
#SELECT catalog.id, code, category_id, category.title AS category, catalog.title, info, details, price, photo, 
#(SELECT AVG(rating) FROM sale WHERE sale.catalog_id = catalog.id) AS avg_rating,
#(SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id) AS sale_quantity
#FROM catalog LEFT JOIN category ON catalog.category_id = category.id
class ViewCatalog(models.Model):
    code = models.CharField(_('code'), max_length=32, blank=True, null=True)
    category_id = models.IntegerField(_('category_id'))
    category = models.CharField(_('category_title'), max_length=128)
    title = models.CharField(_('catalog_title'), max_length=255)
    info = models.CharField(_('info'), max_length=255, blank=True, null=True)
    details = models.TextField(_('catalog_details'), blank=True, null=True)
    price = models.DecimalField(_('price'), max_digits=9, decimal_places=2)
    quantity = models.IntegerField(_('quantity'))
    available = models.IntegerField(_('available'))
    photo = models.ImageField(_('photo'), upload_to='images/', blank=True, null=True)
    avg_rating = models.DecimalField(_('avg_rating'), max_digits=6, decimal_places=2)
    sale_quantity = models.IntegerField(_('sale_quantity'))
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'view_catalog'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),
        ]
        # Сортировка по умолчанию
        ordering = ['title']
        # Таблицу не надо не добавлять не удалять
        managed = False

# Корзина 
class Basket(models.Model):
    basketday = models.DateTimeField(_('basketday'), auto_now_add=True)
    catalog = models.ForeignKey(Catalog, related_name='basket_catalog', on_delete=models.CASCADE)
    price = models.DecimalField(_('price'), max_digits=9, decimal_places=2)
    quantity = models.IntegerField(_('quantity'), default=1)
    user = models.ForeignKey(User, related_name='user_basket', on_delete=models.CASCADE)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'basket'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['basketday']),
        ]
        # Сортировка по умолчанию
        ordering = ['basketday']
    # Сумма по товару
    def total(self):
        return self.price * self.quantity

# Продажа 
class Sale(models.Model):
    saleday = models.DateTimeField(_('saleday'), auto_now_add=True)
    catalog = models.ForeignKey(Catalog, related_name='sale_catalog', on_delete=models.CASCADE)
    price = models.DecimalField(_('price'), max_digits=9, decimal_places=2)
    quantity = models.IntegerField(_('quantity'), default=1)
    user = models.ForeignKey(User, related_name='sale_user', on_delete=models.CASCADE)
    rating = models.IntegerField(_('rating'), blank=True, null=True)
    details = models.TextField(_('review_details'), blank=True, null=True)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'sale'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['saleday']),
        ]
        # Сортировка по умолчанию
        ordering = ['saleday']
    # Сумма по товару
    def total(self):
        return self.price * self.quantity
    def __str__(self):
        # Вывод в тег SELECT 
        return "{} {} {}".format(self.saleday, self.catalog, self.user.username)
        # Таблицу не надо не добавлять не удалять
        #managed = False

# Представление базы данных Продажа (с последним движением по доставке)
# CREATE VIEW view_sale AS
# SELECT sale.id, username, saleday, catalog_id, view_catalog.category, view_catalog.title, info, code, sale.price, quantity, sale.price*quantity AS total, user_id, rating, sale.details,
# (SELECT strftime('%d.%m.%Y',deliveryday) || ' - ' || movement FROM delivery WHERE sale_id = sale.id AND deliveryday = (SELECT MAX(deliveryday) AS Expr1 FROM delivery AS S WHERE  (sale_id = sale.id) )) AS final
# FROM sale LEFT JOIN view_catalog ON sale.catalog_id = view_catalog.id
# LEFT JOIN auth_user ON sale.user_id = auth_user.id
class ViewSale(models.Model):
    username = models.CharField(_('username'), max_length=128)
    saleday = models.DateTimeField(_('saleday'))
    catalog_id = models.IntegerField(_('catalog_id'))
    category = models.CharField(_('category'), max_length=128)
    title = models.CharField(_('catalog_title'), max_length=255)    
    info = models.CharField(_('info'), max_length=255, blank=True, null=True)
    code = models.CharField(_('code'), max_length=32, blank=True, null=True)
    price = models.DecimalField(_('price'), max_digits=9, decimal_places=2)
    quantity = models.IntegerField(_('quantity'))
    total = models.DecimalField(_('total'), max_digits=9, decimal_places=2)
    user_id = models.IntegerField(_('user_id'))
    rating = models.IntegerField(_('rating'), blank=True, null=True)
    details = models.TextField(_('review_details'), blank=True, null=True)
    final = models.TextField(_('final'), blank=True, null=True)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'view_sale'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['saleday']),
        ]
        # Сортировка по умолчанию
        ordering = ['saleday']
        # Таблицу не надо не добавлять не удалять
        managed = False
    # Сумма по товару
    def total(self):
        return self.price * self.quantity
    #def __str__(self):
    #    return "{} {} {}".format(self.category, self.title, self.username)


# Доставка товара
class Delivery(models.Model):
    DELIVERY_CHOICES = (
        (_('Application accepted for processing'),_('Application accepted for processing')),
        (_('Goods in transit'), _('Goods in transit')),
        (_('Stock item'), _('Stock item')),
        (_('The application is closed, the goods have been delivered'), _('The application is closed, the goods have been delivered')),
    )
    sale = models.ForeignKey(Sale, related_name='sale_delivery', on_delete=models.CASCADE)    
    deliveryday = models.DateTimeField(_('deliveryday'), auto_now_add=True)
    movement = models.CharField(_('movement'), max_length=64, choices=DELIVERY_CHOICES, default='М')
    details = models.TextField(_('delivery_details'), blank=True, null=True) 
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'delivery'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['deliveryday']),
        ]
        # Сортировка по умолчанию
        ordering = ['deliveryday']
    def __str__(self):
        # Вывод в тег SELECT 
        return "{} {} {}".format(self.deliveryday, self.sale, self.movement)
