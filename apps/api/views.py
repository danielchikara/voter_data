from rest_framework import generics, serializers, viewsets, filters, status, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from apps.api.models import *
from apps.api.serializers import *
# Create your views here.


class UserLeaderViewSet(viewsets.ModelViewSet):
    """ obtener lider (GET) Crear Lider ('POST')  Actualizar lider('PUT') Eliminar LIDER ('Delete')  """
    queryset = BasicData.objects.filter(
        basic_data_leader__isnull=False).order_by('-id')
    permission_classes = [IsAdminUser]
    authentication_class = (TokenAuthentication)
    serializer_class = ReadBasicDataSerializer

    def create(self, request, *args, **kwargs):
        """ Crear lider ('POST') """
        serializer = BasicLeaderDataSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Saved'}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """ Actualizar info de lider """
        return super().update(request, *args, **kwargs)


class UserVoterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_class = (TokenAuthentication)
    serializer_class = BasicVoterDataSerializer

    def get_queryset(self):
        queryset = BasicData.objects.filter(
            basic_data_voter__isnull=False).order_by('-id')
        return queryset

    def create(self, request, *args, **kwargs):
        """ Crear votante ('POST') """
        serializer = BasicVoterDataSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Saved'}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """ Actualizar info de votante """
        return super().update(request, *args, **kwargs)
