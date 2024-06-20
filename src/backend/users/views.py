from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response 

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs): 
        return super().list(request, *args, **kwargs)
        '''
        content = {
            'Error' : 'Servicio temporalmente deshabilitado'
        }
        return Response(content, status=HTTP_404_NOT_FOUND)
        '''
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)