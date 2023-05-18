from django.urls import path
from authentication_module import views

urlpatterns = [
    path('signup',views.signup, name='signup')
]