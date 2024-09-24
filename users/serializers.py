from django.contrib.auth.hashers import make_password
from rest_framework import serializers as s

from users.models import User, Role


class UserSerializer(s.ModelSerializer):


    class Meta:
        model = User
        fields = ['username', 'password', 'date_of_birth', 'role']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):

        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.role = Role.objects.get(name='user')
        user.save()
        return user

