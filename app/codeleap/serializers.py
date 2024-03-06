from rest_framework import serializers
from .models import Codeleap


class CodeleapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codeleap
        fields = [
            "id",
            "username",
            "created_datetime",
            "title",
            "content",
        ]
        read_only_fields = ["created_datetime"]

    def create(self, validated_data: dict) -> Codeleap:
        return Codeleap.objects.create(**validated_data)

    def update(self, instance: Codeleap, validated_data: dict) -> Codeleap:
        for key, value in validated_data.items():
            if key != "username":
                setattr(instance, key, value)

        instance.save()

        return instance
