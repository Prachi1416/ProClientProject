from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth import get_user_model
User = get_user_model()


class ClientSerializer( serializers.ModelSerializer ):
    created_by = serializers.SlugRelatedField( slug_field='username', read_only=True )
    class Meta:
        model = Client
        exclude = [ 'updated_at' ]


class ClientUpdateSerializer( serializers.ModelSerializer ):
    created_by = serializers.SlugRelatedField( slug_field='username', read_only=True )
    class Meta:
        model = Client
        fields = "__all__"


class ProjectDetailSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Project
        fields = ( 'id', "project_name" )

class ClientDetailSerializer( serializers.ModelSerializer ):
    created_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    projects = ProjectDetailSerializer(read_only=True,many=True)
    class Meta:
        model = Client
        fields = "__all__"



class UserSerializer( serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = [ 'id', 'username' ]


class ProjectSerializer( serializers.ModelSerializer ):
    client = serializers.SlugRelatedField( slug_field='client_name', read_only=True )
    created_by = serializers.SlugRelatedField( slug_field='username', read_only=True )
    users = UserSerializer(many=True,read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_at', 'created_by', 'users', 'client']



class AssignedProjectSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_at', 'created_by']


