from django.urls import path
from authentic import views

urlpatterns = [
    path('signup/',views.signup, name='sign')
]