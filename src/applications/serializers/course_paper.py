from rest_framework import serializers 
from applications.model.stages import Stages
from rest_enumfield import EnumField


class GetCoursePapersQuerySerializer(serializers.Serializer):
    order_by = serializers.CharField(required=False, default='created_at')


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