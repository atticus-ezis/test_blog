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
    path('<int:pk>/<str:model_name>/like', views.like, name='like'),
    path('profile/', views.profile, name="profile"),
    path('create_folder/', views.create_folder, name="create_folder"),
    path('<int:pk>/add_folder/', views.add_blog_to_folder, name="add_to_folder"),
    path('<int:pk>/reader', views.reader, name="reader"),
    path('<int:id>/<str:username>/view_profile', views.view_profile, name="view_profile"),
]

