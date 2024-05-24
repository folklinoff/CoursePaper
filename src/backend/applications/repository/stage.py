
from applications.model.stage import Stage
import sqlite3

class StageRepository:
    def create(self, stage: Stage) -> None:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO StageModel (
                stage_id, 
                stage_name, 
                stage_created_at, 
                stage_course_paper_id
            ) VALUES (?, ?, ?, ?)
        """, (stage.id, stage.name.value, str(stage.created_at), stage.course_paper_id))
        conn.commit()
        conn.close()


    def get_by_course_paper_id(self, course_paper_id: str, limit, offset) -> list[Stage]:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM StageModel
            WHERE stage_course_paper_id = ?
            LIMIT ? OFFSET ?
        """, (course_paper_id, limit, offset))
        rows = cursor.fetchall()
        conn.close()
        return [Stage.from_tuple(row) for row in rows]


    def get_count_by_course_paper_id(self, course_paper_id: str) -> list[Stage]:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM StageModel
            WHERE stage_course_paper_id = ?
        """, (course_paper_id,))
        count = cursor.fetchone()[0]
        conn.close()
        return count
    

stage_repository = StageRepository()



