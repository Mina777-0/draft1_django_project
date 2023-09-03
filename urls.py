from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordChange

urlpatterns = [
    path('', views.log_in, name="log_in"),
    path('index', views.index, name="index"),
    path('log_out', views.log_out, name="log_out"),
    path('signup', views.signup, name="signup"),
    path('<int:trip_id>', views.passengers, name="passengers"),
    path('password', PasswordChange.as_view(template_name= "app/passchange.html"), name="password"),
    path('password_success', views.password_success, name="password_success"),
]
