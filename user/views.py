from rest_framework import generics
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer


@api_view(['get'])
def api_root(request, format = None):
    return Response({
        'auth': reverse('auth', request = request, format = format),
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id = user.id)

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        obj = super().get_object()

        if obj == user or user.is_staff or user.is_superuser:
            return obj
        else:
            raise PermissionDenied("You cannot access this user's details.")

class Register(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer

     def perform_create(self, serializer):
         user = serializer.save()

         token, created = Token.objects.get_or_create(user = user)

         self.response_data = {
             "user": {
                 "id": user.id,
                 "username" : user.name,
                 "email": user.email,
                 "full_name": user.full_name
             },
             "token": token.key
         }

     def create(self, request, *args, **kwargs):
         super().create(request, *args, **kwargs)
         return Response(self.response_data)

class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            raise AuthenticationFailed("Invalid Username of Password")
        else:
            token,create = Token.objects.get_or_create(user = user)
            return Response({
             "user": {
                 "id": user.id,
                 "username" : user.name,
                 "email": user.email,
                 "full_name": user.full_name
             },
             "token": token.key
         })