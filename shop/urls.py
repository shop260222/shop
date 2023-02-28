"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings 
from django.conf.urls.static import static 
from django.conf.urls import include

from product import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('report/index/', views.report_index, name='report_index'),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    
    path('category/index/', views.category_index, name='category_index'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', views.category_delete, name='category_delete'),
    path('category/read/<int:id>/', views.category_read, name='category_read'),

    path('catalog/index/<int:invoice_id>/', views.catalog_index, name='catalog_index'),
    path('catalog/list/', views.catalog_list, name='catalog_list'),
    path('catalog/create/<int:invoice_id>/', views.catalog_create, name='catalog_create'),
    path('catalog/edit/<int:id>/<int:invoice_id>/', views.catalog_edit, name='catalog_edit'),
    path('catalog/delete/<int:id>/<int:invoice_id>/', views.catalog_delete, name='catalog_delete'),
    path('catalog/read/<int:id>/<int:invoice_id>/', views.catalog_read, name='catalog_read'),
    path('catalog/details/<int:id>/', views.catalog_details, name='catalog_details'),    
    path('catalog/basket/', views.basket, name='basket'),
    path('catalog/buy/', views.buy, name='buy'),
    
    path('basket/delete/<int:id>/', views.basket_delete, name='basket_delete'),

    path('delivery/list/', views.delivery_list, name='delivery_list'),
    path('delivery/index/<int:id>/', views.delivery_index, name='delivery_index'),
    path('delivery/create/<int:sale_id>/', views.delivery_create, name='delivery_create'),
    path('delivery/edit/<int:id>/', views.delivery_edit, name='delivery_edit'),
    path('delivery/delete/<int:id>/', views.delivery_delete, name='delivery_delete'),
    path('delivery/read/<int:id>/', views.delivery_read, name='delivery_read'),

    path('organization/index/', views.organization_index, name='organization_index'),
    path('organization/create/', views.organization_create, name='organization_create'),
    path('organization/edit/<int:id>/', views.organization_edit, name='organization_edit'),
    path('organization/delete/<int:id>/', views.organization_delete, name='organization_delete'),
    path('organization/read/<int:id>/', views.organization_read, name='organization_read'),

    path('invoice/index/', views.invoice_index, name='invoice_index'),
    path('invoice/create/', views.invoice_create, name='invoice_create'),
    path('invoice/edit/<int:id>/', views.invoice_edit, name='invoice_edit'),
    path('invoice/delete/<int:id>/', views.invoice_delete, name='invoice_delete'),
    path('invoice/read/<int:id>/', views.invoice_read, name='invoice_read'),
    
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
