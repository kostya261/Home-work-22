"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

# Маршруты
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product_detail/<int:product_id>/', cache_page(60)(views.ProductDetailView.as_view()), name='detail_product'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('product_edit/<int:product_id>/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product_delete/<int:product_id>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', views.ProductsByCategoryView.as_view(), name='products_by_category'),
]
