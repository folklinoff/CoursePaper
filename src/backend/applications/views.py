from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from applications.decorators.error_handler import handle_error
from applications.model.stages import Stages
from applications.model.errors import UnprocessableEntityError
from applications.serializers.errors import *
from applications.serializers.course_paper import *
from applications.serializers.stage import *
from rest_framework import status
from rest_framework.response import Response
from applications.services.course_paper import course_paper_service
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.
@extend_schema_view(
    create = extend_schema(
        description='Create course paper',
        request=CreateCoursePaperDTOSerializer,
        responses={
            status.HTTP_201_CREATED: CoursePaperSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestErrorSerializer,
            status.HTTP_422_UNPROCESSABLE_ENTITY: UnprocessableEntityErrorSerializer,
        }
    ),
    list = extend_schema(
        description='Create course paper',
        parameters=[GetItemsSerializer],
        responses={
            status.HTTP_200_OK: CoursePapersListSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestErrorSerializer,
            status.HTTP_422_UNPROCESSABLE_ENTITY: UnprocessableEntityErrorSerializer,
        }
    ),
    update_stage = extend_schema(
        description='Create course paper',
        request=UpdateStageDTOSerializer,
        responses={
            status.HTTP_200_OK: CoursePaperSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestErrorSerializer,
            status.HTTP_422_UNPROCESSABLE_ENTITY: UnprocessableEntityErrorSerializer,
        }
    ),
    list_stages = extend_schema(
        description='Create course paper',
        parameters=[GetItemsSerializer],
        responses={
            status.HTTP_200_OK: CoursePaperSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestErrorSerializer,
            status.HTTP_422_UNPROCESSABLE_ENTITY: UnprocessableEntityErrorSerializer,
        }
    ),
)
class CoursePapersViewSet(ViewSet):
    @handle_error
    def create(self, request):
        create_dto_ser = CreateCoursePaperDTOSerializer(data=request.data)
        if not create_dto_ser.is_valid():
            raise UnprocessableEntityError(message=create_dto_ser.errors)
        course_paper = course_paper_service.create(**create_dto_ser.data)
        return Response(CoursePaperSerializer(course_paper).data, status=status.HTTP_201_CREATED)
    

    @handle_error
    def list(self, request):
        get_query_ser = GetItemsSerializer(data=request.query_params)
        if not get_query_ser.is_valid():
            raise UnprocessableEntityError(message=get_query_ser.errors)
        course_papers = course_paper_service.list(**get_query_ser.data)
        return Response(CoursePapersListSerializer(course_papers).data, status=status.HTTP_200_OK)
    

    @action(detail=False)
    @handle_error
    def update_stage(self, request, id):
        update_stage_dto_ser = UpdateStageDTOSerializer(data=request.data)
        if not update_stage_dto_ser.is_valid():
            raise UnprocessableEntityError(message=update_stage_dto_ser.errors)
        stage = course_paper_service.update_stage(id, Stages(update_stage_dto_ser.data['stage']))
        return Response(StageDetailsSerializer(stage).data, status=status.HTTP_200_OK)
    

    @action(detail=True)
    @handle_error
    def list_stages(self, request, id):
        get_query_ser = GetItemsSerializer(data=request.query_params)
        if not get_query_ser.is_valid():
            raise UnprocessableEntityError(message=get_query_ser.errors)
        stages = course_paper_service.list_stages(id, **get_query_ser.data)
        return Response(StagesListSerializer(stages).data, status=status.HTTP_200_OK)
    

    @action(detail=True)
    @handle_error
    def count(self, _):
        count = course_paper_service.get_count()
        return Response(CountMapSerializer(count).data, status=status.HTTP_200_OK)
    

    @action(detail=True)
    @handle_error
    def count_stages(self, _, id):
        count = course_paper_service.get_stages_count(id)
        return Response(CountMapSerializer(count).data, status=status.HTTP_200_OK)