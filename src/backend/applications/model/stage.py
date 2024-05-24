# Create your models here.
from datetime import datetime
from uuid import uuid4

from applications.model.course_paper import CoursePaper
from applications.model.stages import Stages


class Stage:
    def __init__(self, course_paper_id: str, name: Stages = None, id: str = None, created_at: datetime = None) -> None:
        self.id: str = str(id) if id is not None else str(uuid4())
        self.name: Stages = Stages.PREPARING if name is None else Stages(name)
        self.course_paper_id: str = course_paper_id
        self.created_at: datetime = created_at if created_at is not None else datetime.now()

    def from_tuple(model: tuple):
        stage = Stage(None)
        (stage.id, stage.name, stage.created_at, stage.course_paper_id) = model
        stage.id = str(stage.id)
        stage.name = Stages(stage.name)
        stage.created_at = datetime.strptime(stage.created_at, '%Y-%m-%d %H:%M:%S.%f')
        stage.course_paper_id = str(stage.course_paper_id)
        return stage