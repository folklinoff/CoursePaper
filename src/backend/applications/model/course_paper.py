from applications.model.stages import Stages
from uuid import uuid4
from datetime import datetime


class CoursePaper:
    def __init__(self, name, student_id, current_stage: Stages, id: str = None, created_at: datetime = None) -> None:
        self.id: str = id if id is not None else str(uuid4())
        self.name: str = name
        self.student_id: str = str(student_id)
        self.current_stage: Stages = Stages(current_stage) if not isinstance(current_stage, Stages) else current_stage
        self.created_at: datetime = created_at if created_at is not None else datetime.now()

    def from_tuple(model: tuple):
        course_paper = CoursePaper(None, None, Stages.PREPARING)
        (course_paper.id, course_paper.name, course_paper.student_id, course_paper.created_at, course_paper.current_stage) = model
        course_paper.id = course_paper.id
        course_paper.name = course_paper.name
        course_paper.student_id = course_paper.student_id
        course_paper.created_at = datetime.strptime(course_paper.created_at, '%Y-%m-%d %H:%M:%S.%f')
        course_paper.current_stage = Stages(course_paper.current_stage)
        return course_paper