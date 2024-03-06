from rest_framework import serializers


from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key != "username":
                setattr(instance, key, value)

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "created_datetime",
            "title",
            "content",
        ]
        read_only_fields = ["created_datetime"]
