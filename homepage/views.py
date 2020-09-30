from homepage.models import BoastsRoasts, MyUser

from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from homepage.serializers import BoastsRoastsSerializer, MyUserSerializer

# Create your views here.


class BoastsRoastsViewSet(viewsets.ModelViewSet):
    queryset = BoastsRoasts.objects.all()
    serializer_class = BoastsRoastsSerializer

    @action(detail=False)
    def Boasts(self, request):
        just_boasts = BoastsRoasts.objects.filter(
            post_type='boast').order_by('submission_time')
        serializer = self.get_serializer(just_boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def HighestRated(self, request):
        all_posts = BoastsRoasts.objects.all().order_by('total_votes')

        serializer = self.get_serializer(all_posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def Roasts(self, request):
        just_roasts = BoastsRoasts.objects.filter(
            post_type='roast').order_by('submission_time')
        serializer = self.get_serializer(just_roasts, many=True)
        return Response(serializer.data)


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.filter(is_active=True)
    serializer_class = MyUserSerializer
