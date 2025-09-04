from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterUserAPI( CreateAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
