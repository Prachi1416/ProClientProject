from django.urls import path
from . import views

urlpatterns = [
    path( 'clients/', views.ClientListCreateAPI.as_view(), name='client-list-create' ),
    path( 'clients/<pk>/', views.ClientDetailAPI.as_view(), name='client-detail' ),
    path( 'client/<pk>/projects/', views.ProjectAPI.as_view(), name='client-projects' ),
    path( 'projects/', views.AssignedProjectsAPI.as_view(), name='assigned-projects' ),

]
