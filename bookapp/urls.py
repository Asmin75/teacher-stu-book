from django.urls import path
from bookapp import views

urlpatterns = [
    path('register/', views.registration_view),
    path('login/', views.login),
    path('books/', views.BookListview.as_view()),
    path('books_detail/<int:pk>', views.BookDetailView.as_view()),
]