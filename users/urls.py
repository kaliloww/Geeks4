from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path("users/register/", RegisterView.as_view(), name='register'),
    
]