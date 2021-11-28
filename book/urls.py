from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookList.as_view()),
    path('<int:id>/', views.BookDetail.as_view()),
]