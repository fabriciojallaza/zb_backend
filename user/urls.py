from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('', views.UserView.as_view({'get': 'list'}), name='user_list'),
    path('authtoken/', views.TokenCreate.as_view(), name='authtoken'),
    path('manage/create/', views.UserCreate.as_view(), name='user_create'),
    path('manage/<int:pk>/', views.UserManage.as_view(), name='user_manage'),
]
