from rest_framework import generics, serializers, viewsets, filters, status, permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from apps.api.models import *
from apps.api.serializers import *
# Create your views here.


class UserLeaderViewSet(viewsets.ModelViewSet):
    """ obtener lider (GET) Crear Lider ('POST')  Actualizar lider('PUT') Eliminar LIDER ('Delete')  """
    queryset = Leader.objects.filter(basic_data__is_active = True)
    permission_classes  = [IsAdminUser]
    authentication_class = (TokenAuthentication)
    
    def create(self, request, *args, **kwargs):
        """ Crear lider ('POST') """
        data = request.data 
        serializer = UserLeaderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'status': 'Saved'}, status=status.HTTP_201_CREATED)
        return super().create(request, *args, **kwargs) 