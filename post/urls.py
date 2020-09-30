from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('create', views.create, name='create'),
    path('update', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('<str:id>', views.getbyid, name='getbyid'),
]