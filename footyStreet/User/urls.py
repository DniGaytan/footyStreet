from django.urls import path
from User import views

app_name = "user"

urlpatterns = [
    path('register/', views.registerUser, name="registerPath"),
    path('login/', views.loginUser, name="loginPath"),
    path('logout/', views.logoutUser, name="logoutPath"),

]
