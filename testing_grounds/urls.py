from django.urls import path, include
from . import views
from .views import index, BlogCreationView

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('submit/', views.form, name="form"),
    path('<int:pk>/delete', views.delete, name="delete"),
    path('<int:pk>/edit', views.edit, name='edit'),
]