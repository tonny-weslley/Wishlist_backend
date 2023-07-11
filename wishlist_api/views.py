from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.contrib.auth import authenticate

from rest_framework.parsers import JSONParser 
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.

from .models import Wish, List, User, Usuario
from .serializer import WishSerializer, ListSerializer, UsuarioSerializer, LoginSerializer, CadastroSerializer

#metodo para pegar usuario apartir do token
def get_user_from_token(request):
    try:
        auth = TokenAuthentication()
        user, token = auth.authenticate(request)
        return user
    except AuthenticationFailed:
        return None

#user viewset
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    

class WishViewSet(viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = [AllowAny]

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [AllowAny]

class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'],serializer_class=CadastroSerializer, url_path='cadastro')
    def cadastro(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        confirmed_password = request.data.get('confirmed_password')
        username = request.data.get('username') 
        cover_image = request.data.get('cover_image')

        user = User.objects.filter(username=username).first()

        #verifica se o usuario já existe
        if  (user is not None):
            return Response({'error': 'Usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            #verifica se as passwords são iguais
            if password != confirmed_password:
                return Response({'error': 'passwords não conferem'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                #cria o usuario
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
                user.save()
                u = Usuario.objects.create(user=user, cover_image=cover_image, joined_in=datetime.datetime.now())
                u.save()
                return Response({'success': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'],serializer_class=LoginSerializer, url_path='login')
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        user = User.objects.filter(username=username)
        if (user):
            user = authenticate(username=username, password=password)
            if user is not None:
                return Response({'username': user.username,"nome":user.first_name}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Usuário ou senha incorretos'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Usuário não existe'}, status=status.HTTP_400_BAD_REQUEST)