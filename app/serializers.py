from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Question, Choice, UserSelection


class UserSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSelection
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    userSelections = UserSelectionSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
