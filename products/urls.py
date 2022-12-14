from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view({'get': 'list'}), name='products'),
    path('<int:pk>/', views.ProductView.as_view(), name='product_view'),
    path('create/', views.ProductCreate.as_view(), name='product_create'),
    path('control/<int:pk>/', views.ProductControl.as_view(), name='product_control'),

]
#urlpatterns = format_suffix_patterns(urlpatterns)

