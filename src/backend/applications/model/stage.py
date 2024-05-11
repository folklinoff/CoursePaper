# Create your models here.
from datetime import datetime
from uuid import UUID, uuid4

from applications.model.course_paper import CoursePaper
from applications.model.stages import Stages


class Stage:
    def __init__(self, course_paper: CoursePaper, name: Stages = None, id: UUID = None, created_at: datetime = None) -> None:
        self.id: UUID = id if id is not None else uuid4()
        self.name: Stages = Stages.PREPARING if name is None else Stages(name)
        self.course_paper: CoursePaper = course_paper
        self.created_at: datetime = created_at if created_at is not None else datetime.now()
