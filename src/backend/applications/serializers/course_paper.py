from rest_framework import serializers 
from applications.model.stages import Stages
from rest_enumfield import EnumField


class GetItemsSerializer(serializers.Serializer):
    limit = serializers.IntegerField(min_value=10, max_value=100, default=20)
    offset = serializers.IntegerField(default=0)


class CreateCoursePaperDTOSerializer(serializers.Serializer):
    student_id = serializers.UUIDField()
    name = serializers.CharField()


class CoursePaperSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    student_id = serializers.UUIDField()
    current_stage = EnumField(choices=Stages)
    created_at = serializers.DateTimeField()


class CoursePapersListSerializer(serializers.Serializer):
    course_papers = CoursePaperSerializer(many=True)