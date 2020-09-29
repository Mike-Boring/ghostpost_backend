from homepage.models import BoastsRoasts, MyUser

from rest_framework import viewsets

from homepage.serializers import BoastsRoastsSerializer, MyUserSerializer

# Create your views here.


class BoastsRoastsViewSet(viewsets.ModelViewSet):
    queryset = BoastsRoasts.objects.all()
    serializer_class = BoastsRoastsSerializer


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.filter(is_active=True)
    serializer_class = MyUserSerializer
