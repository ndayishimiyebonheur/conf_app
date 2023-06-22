from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView, name='Conference'),
    path('create/', views.CreateView, name='Conference'),
    path('update/', views.UpdateView, name='Conference'),
    path('delete/', views.DeleteView, name='Conference'),
    path('deleteConfirm/', views.DeleteConfirmView, name='Conference'),
]
