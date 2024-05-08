from applications.model.stages import Stages

from datetime import datetime
from uuid import UUID, uuid4

class CoursePaper:
    def __init__(self, name, student_id, current_stage: Stages, id: UUID = None, created_at: datetime = None) -> None:
        self.id: UUID = id if id is not None else uuid4()
        self.name: str = name
        self.student_id: UUID = student_id
        self.current_stage: Stages = Stages(current_stage)
        self.created_at: datetime = created_at if created_at is not None else datetime.now()