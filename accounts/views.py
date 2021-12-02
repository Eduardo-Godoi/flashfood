from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from utils.geolocation import geocoding

from accounts.models import User
from accounts.serializers import LoginSerializer, UserSerializer


class CreateUserView(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer(self, *args, **kwargs):
        street = self.request.data.get('street', None)
        district = self.request.data.get('district', None)
        number = self.request.data.get('number', None)
        city = self.request.data.get('city', None)
        state = self.request.data.get('state', None)
        cep = self.request.data.get('cep', None)
        coordinates = geocoding(self.request.data)

        self.request.data['adress'] = {
            'street': street,
            'district': district,
            'number': number,
            'city': city,
            'state': state,
            'cep': cep,
            'coordinates': coordinates
        }

        return super().get_serializer(*args, **kwargs)

class LoginUserVIew(APIView):

    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)

        user = authenticate(**login_serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})
        
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
