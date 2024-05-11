from django.db import models

from applications.model.stages import Stages


class CoursePaperModel(models.Model):
    id = models.UUIDField(name='course_paper_id', primary_key=True)
    name =  models.CharField(name='course_paper_name', max_length=100)
    student_id = models.UUIDField(name='course_paper_student_id')
    created_at = models.DateTimeField(name='course_paper_created_at')
    current_stage = models.CharField(name='course_paper_current_stage', choices=[(e.value, e.value) for e in Stages], max_length=12)


class StageModel(models.Model):
    id = models.UUIDField(name='stage_id', primary_key=True)
    name = models.CharField(name='stage_name', choices=[(e.value, e.value) for e in Stages], max_length=12)
    created_at = models.DateTimeField(name='stage_created_at')
    course_paper = models.ForeignKey(CoursePaperModel, on_delete=models.DO_NOTHING, name='stage_course_paper')