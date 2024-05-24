from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField()


class UnprocessableEntityErrorSerializer(serializers.Serializer):
    error = ErrorSerializer()


class BadRequestErrorSerializer(serializers.Serializer):
    error = serializers.CharField()

