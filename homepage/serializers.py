from rest_framework import serializers

from homepage.models import BoastsRoasts, MyUser


class BoastsRoastsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastsRoasts
        fields = [
            'id',
            'post_type',
            'post_text',
            'up_votes',
            'down_votes',
            'submission_time',
            'last_updated',
            'total_votes'
        ]


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'id',
            'username',
            'is_active'
        ]
