from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Book


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['user_type', 'email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('name', 'content', 'owner')




