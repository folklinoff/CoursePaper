from uuid import UUID
from applications.model.stage import Stage
from applications.models import StageModel
from applications.repository.mapper import model_to_stage, stage_to_model


class StageRepository:
    def create(self, stage: Stage) -> None:
        stage_to_model(stage).save()

    def get_by_course_paper_id(self, course_paper_id: UUID) -> list[Stage]:
        return map(model_to_stage, list(StageModel.objects.all().filter(stage_course_paper_id=course_paper_id)))


stage_repository = StageRepository()



