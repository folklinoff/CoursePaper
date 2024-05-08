from rest_enumfield import EnumField
from rest_framework import serializers

from applications.model.stages import Stages


class UpdateStageDTOSerializer(serializers.Serializer):
    stage = EnumField(choices=Stages)


class StageDetailsSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = EnumField(choices=Stages)
    course_paper_id = serializers.UUIDField()
    created_at = serializers.DateTimeField()


class StagesListSerializer(serializers.Serializer):
    stages = StageDetailsSerializer(many=True)