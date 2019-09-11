from django.urls import path
from bookapp import views

urlpatterns = [
    path('register/', views.registration_view),
    path('login/', views.login),

]