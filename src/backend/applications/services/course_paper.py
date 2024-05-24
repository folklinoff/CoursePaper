
from applications.model.course_paper import CoursePaper
from applications.model.stage import Stage
from applications.model.stages import Stages
from applications.repository.course_paper import course_paper_repository
from applications.repository.stage import stage_repository

class CoursePapersService:
    def create(self, name: str, student_id: str) -> CoursePaper:
        course_paper = CoursePaper(name, student_id, Stages.PREPARING)
        course_paper_repository.create(course_paper)
        stage_repository.create(Stage(course_paper.id, Stages.PREPARING))
        return course_paper
    
    
    def list(self, limit, offset) -> dict[str, list[CoursePaper]]:
        return {'course_papers': course_paper_repository.list(limit, offset)}
    
    
    def update_stage(self, id: str, stage: Stages):
        course_paper = course_paper_repository.get(id)
        real_stage = Stage(course_paper_id=course_paper.id, name=stage)
        stage_repository.create(real_stage)
        course_paper_repository.update_stage(real_stage.course_paper_id, real_stage.name.value)
        return real_stage


    def list_stages(self, course_paper_id: str, limit, offset):
        stages = stage_repository.get_by_course_paper_id(course_paper_id, limit, offset)
        print(stages)
        print(len(stages))
        if len(stages) == 0:
            raise KeyError(f"course paper with id {course_paper_id} does not exist")
        return {'stages': stages}
    
    
    def get_count(self) -> dict[str, int]:
        return {'count': course_paper_repository.get_count()}
    

    def get_stages_count(self, course_paper_id: int) -> dict[str, int]:
        return {'count': stage_repository.get_count_by_course_paper_id(course_paper_id)}




course_paper_service: CoursePapersService = CoursePapersService()