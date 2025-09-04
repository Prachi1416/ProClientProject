from rest_framework import generics, response
from .serializers import ( ClientSerializer, ClientUpdateSerializer,
                           ProjectSerializer, ClientDetailSerializer,
                            AssignedProjectSerializer
                           )
from .models import Client, Project
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import NotFound


class ClientListCreateAPI( generics.ListCreateAPIView ):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save( created_by = self.request.user )


class ClientDetailAPI( generics.RetrieveUpdateDestroyAPIView ):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ClientDetailSerializer
        return super().get_serializer_class()



class ProjectAPI( generics.CreateAPIView ):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        client_id = self.kwargs.get('pk')
        try:
            client = Client.objects.get(id=client_id)
            project = serializer.save(created_by=self.request.user, client=client)
            users = self.request.data.get('users', [])
            for user in users:
                user_id = user.get('id')
                userObj = User.objects.get(id=user_id)
                project.users.add(userObj)
        except Client.DoesNotExist:
            raise NotFound("Client not found")


class AssignedProjectsAPI( generics.ListAPIView ):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    queryset = Project.objects.all()
    serializer_class = AssignedProjectSerializer

    def get_queryset(self):
        return Project.objects.filter( users = self.request.user )
