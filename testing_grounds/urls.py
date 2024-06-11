from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('submit/', views.form, name="form"),
    path('<int:pk>/comment', views.comment, name="comment"),
    path('<int:pk>/<str:model_name>/delete', views.delete, name="delete"),
    path('<int:pk>/<str:model_name>/edit', views.edit, name='edit'),
]

