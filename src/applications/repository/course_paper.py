from uuid import UUID
from applications.model.course_paper import CoursePaper
from applications.model.stage import Stage
from applications.model.stages import Stages
from applications.models import CoursePaperModel
from applications.repository.mapper import course_paper_to_model, model_to_course_paper


class CoursePaperRepository:
    def create(self, course_paper: CoursePaper) -> None:
        course_paper_to_model(course_paper).save()
    
    
    def list(self, order_by) -> list[CoursePaper]:
        return map(model_to_course_paper, list(CoursePaperModel.objects.all().order_by('course_paper_' + order_by)))
    
    
    def update_stage(self, course_paper_id: UUID, stage: Stages) -> None:
        model = CoursePaperModel.objects.get(pk=course_paper_id)
        model.course_paper_current_stage = stage
        model.save(force_update=True)
    

    def get(self, course_paper_id: UUID) -> CoursePaper:
        return model_to_course_paper(CoursePaperModel.objects.get(pk=course_paper_id))


course_paper_repository = CoursePaperRepository()