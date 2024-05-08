from uuid import UUID
from applications.model.course_paper import CoursePaper
from applications.model.stage import Stage
from applications.model.stages import Stages
from applications.repository.course_paper import course_paper_repository
from applications.repository.stage import stage_repository

class CoursePapersService:
    def create(self, name: str, student_id: UUID) -> CoursePaper:
        course_paper = CoursePaper(name, student_id, Stages.PREPARING)
        course_paper_repository.create(course_paper)
        stage_repository.create(Stage(course_paper, Stages.PREPARING))
        return course_paper
    
    
    def list(self, order_by) -> dict[str, list[CoursePaper]]:
        if order_by is None:
            order_by = 'created_at'
        return {'course_papers': course_paper_repository.list(order_by)}
    
    
    def update_stage(self, id: UUID, stage: Stages):
        course_paper = course_paper_repository.get(id)
        real_stage = Stage(course_paper=course_paper, name=stage)
        stage_repository.create(real_stage)
        course_paper_repository.update_stage(real_stage.course_paper.id, real_stage.name.value)
        return course_paper_repository.get(real_stage.course_paper.id)


    def stage_model_to_details(self, model: Stage) -> dict[str]:
        m = model.__dict__.copy()
        m.pop('course_paper')
        m['course_paper_id'] = model.course_paper.id
        return m


    def list_stages(self, course_paper_id: UUID):
        stages = stage_repository.get_by_course_paper_id(course_paper_id)
        if len(stages) == 0:
            raise KeyError
        return {'stages': 
                list(map(self.stage_model_to_details, stages))
        }




course_paper_service: CoursePapersService = CoursePapersService()