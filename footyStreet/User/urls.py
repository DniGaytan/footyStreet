from django.urls import path
from User import views

app_name = "user"

urlpatterns = [
    path('register/', views.register, name="registerPath"),
    path('login/', views.login, name="loginPath"),
    path('logout/', views.logout, name="logoutPath"),

]
