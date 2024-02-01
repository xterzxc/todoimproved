from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, generics
from rest_framework.permissions import BasePermission
from .serializers import RegisterSerializer
from .models import CustomUser


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class IsPremium(BasePermission):
    def has_premium(self, request, view, obj):
        return request.user.is_authenticated and request.user.premium

class AddContributorView(generics.UpdateAPIView):
    '''
    Add contributors fitch for premium users
    '''
    permission_classes = [IsPremium]

    def add_contributor(self, request, *args, **kwargs):
        pass


