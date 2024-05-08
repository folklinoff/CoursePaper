from applications.model.course_paper import CoursePaper
from applications.model.stage import Stage
from applications.models import CoursePaperModel, StageModel


def course_paper_to_model(course_paper: CoursePaper) -> CoursePaperModel:
    m = {
            "course_paper_" + key: val
            for key, val in course_paper.__dict__.items() if key != 'stage'
        }
    m.update({'course_paper_current_stage': course_paper.current_stage.value})
    return CoursePaperModel(
        **m
    )


def model_to_stage(model: StageModel) -> Stage:
    m = {key.removeprefix('stage_'): val for key, val in model.__dict__.items() if key not in {'_state', 'stage_course_paper_id'}}
    m.update({'course_paper': model_to_course_paper(CoursePaperModel.objects.get(pk=model.stage_course_paper_id))})
    return Stage(
        **m
    )


def model_to_course_paper(course_paper: CoursePaperModel) -> CoursePaper:
    m = {
        key.removeprefix('course_paper_'): val for key, val in course_paper.__dict__.items() if key not in {'_state', 'course_paper_current_stage'} 
    }
    m.update({'current_stage': str(course_paper.course_paper_current_stage)})
    return CoursePaper(
        **m
    )


def stage_to_model(stage: Stage) -> StageModel:
    m =  {'stage_' + key: val for key, val in stage.__dict__.items() if key not in {'course_paper', 'name'}}
    m.update({'stage_course_paper_id': stage.course_paper.id})
    m.update({'stage_name': stage.name.value})
    return StageModel(
        **m
    )