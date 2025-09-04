from django.urls import path
from .views import RegisterUserAPI

urlpatterns = [
    path( 'signup/', RegisterUserAPI.as_view(), name='signup' )
]
