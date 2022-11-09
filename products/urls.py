from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    path('list/', views.ProductList.as_view(), name='products-list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

