from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('sign-in', views.signIn, name=""),
    path('sign-up', views.signUp, name=""),
    path('posts/<int:pk>/', views.postDetail, name='post_detail'),
    path('sign-out/', views.signOut, name='sign-out'),
]
