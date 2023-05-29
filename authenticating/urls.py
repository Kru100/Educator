from django.urls import path
from .views import *

urlpatterns = [
    path('signup', registerAPI.as_view()),
    path('verification', verificationAPI.as_view())
]