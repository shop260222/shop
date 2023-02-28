from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput
from .models import Category, Catalog, Delivery, Organization, Invoice
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re
import datetime
from django.utils import timezone
import pytz

# При разработке приложения, использующего базу данных, чаще всего необходимо работать с формами, которые аналогичны моделям.
# В этом случае явное определение полей формы будет дублировать код, так как все поля уже описаны в модели.
# По этой причине Django предоставляет вспомогательный класс, который позволит вам создать класс Form по имеющейся модели
# атрибут fields - указание списка используемых полей, при fields = '__all__' - все поля
# атрибут widgets для указания собственный виджет для поля. Его значением должен быть словарь, ключами которого являются имена полей, а значениями — классы или экземпляры виджетов.
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title',]
        widgets = {
            'title': TextInput(attrs={"size":"100"}),            
        }
        labels = {
            'title': _('category_title'),            
        }
    # Метод-валидатор для поля title
    def clean_title(self):
        data = self.cleaned_data['title']
        # Ошибка если начинается не с большой буквы
        if data.istitle() == False:
            raise forms.ValidationError(_('Value must start with a capital letter'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    
# Каталог магазина
class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('code', 'category', 'title', 'info', 'details', 'price', 'quantity', 'photo')
        widgets = {
            'code': TextInput(attrs={"size":"30"}),
            'category': forms.Select(attrs={'class': 'chosen'}),
            'title': TextInput(attrs={"size":"50"}),
            'info': TextInput(attrs={"size":"50"}),
            'details': Textarea(attrs={'cols': 50, 'rows': 5}),            
            'price': NumberInput(attrs={"size":"10"}),
            'quantity': NumberInput(attrs={"size":"10"}),            
        }
        labels = {
            'code': _('code'),
            'category': _('category'),
            'title': _('catalog_title'),
            'info': _('info'),
            'details': _('details'),
            'price': _('price'),
            'quantity': _('quantity'),
        }
    # Метод-валидатор для поля numb
    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        #print(data)
        # Проверка номер больше нуля
        if data <= 0:
            raise forms.ValidationError(_('Quantity must be greater than zero'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    # Метод-валидатор для поля price
    def clean_price(self):
        data = self.cleaned_data['price']
        #print(data)
        # Проверка номер больше нуля
        if data <= 0:
            raise forms.ValidationError(_('Price must be greater than zero'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data        

# Доставка
class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('movement', 'details')
        widgets = {
            'details': Textarea(attrs={'cols': 50, 'rows': 5}),            
        }
        labels = {
            'movement': _('movement'),
            'details': _('details'),            
        }
    # Метод-валидатор для поля dateis
    def clean_deliveryday(self):
        data = self.cleaned_data['deliveryday']
        #print(data)
        #print(timezone.now())
        # Проверка даты (не больше текущей даты-времени)
        if data > timezone.now():
            raise forms.ValidationError(_('Cannot be greater than the current date'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data        

# Организации 
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ('title', 'address', 'phone',)
        widgets = {
            'title': TextInput(attrs={"size":"100"}),
            'address': TextInput(attrs={"size":"50"}),
            'phone': TextInput(attrs={"size":"50", "type":"tel"}),            
        }
        labels = {
            'title': _('title'),
            'address': _('address'),
            'phone': _('phone'),            
        }
    # Метод-валидатор для поля phone
    def clean_phone(self):
        data = self.cleaned_data['phone']
        result = re.match(r'^((\+?7|8)[ \-] ?)?((\(\d{3}\))|(\d{3}))?([ \-])?(\d{3}[\- ]?\d{2}[\- ]?\d{2})$', data)
        #print('result ',bool(result))  
        # Проверка телефонного номера по маске с помощью регулярного выражения
        if bool(result) == False:
            raise forms.ValidationError(_('Enter your phone number in the format +7-ХХХ-ХХХ-ХХХХ or 8-ХХХ-ХХХ-ХХХХ'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data

# Приходные накладные  
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('organization', 'datei', 'numb',)
        widgets = {
            'organization': forms.Select(attrs={'class': 'chosen'}),
            'datei': DateInput(attrs={"type":"date"}),
            'numb': DateInput(attrs={"type":"number"}),
        }
        labels = {
            'organization': _('organization'),
            'datei': _('datei'),
            'numb': _('numb'),            
        }
    # Метод-валидатор для поля dateis
    def clean_datei(self):
        data = self.cleaned_data['datei']
        #print(data)
        #print(timezone.now())
        # Проверка даты (не больше текущей даты-времени)
        if data > timezone.now():
            raise forms.ValidationError(_('Cannot be greater than the current date'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    # Метод-валидатор для поля numb
    def clean_numb(self):
        data = self.cleaned_data['numb']
        #print(data)
        # Проверка номер больше нуля
        if data <= 0:
            raise forms.ValidationError(_('The number must be greater than zero'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data        
    
# Форма регистрации
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
