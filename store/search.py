from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import Permission ,Group

from rest_framework import viewsets,response
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.decorators import api_view,action,permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny
# from rest_framework.parsers import MultiPartParser

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import *
from .models import *




class CommandeSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client_id__email','client_id__phone_number','transaction_id']


class PieceSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset  = Piece.objects.all()
    serializer_class = PieceSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields= ['name','modele','description','id_cathegorie__name']
    search_fields = ('name','modele','description','=id_cathegorie__name')

