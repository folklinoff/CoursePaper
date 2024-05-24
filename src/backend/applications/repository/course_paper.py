
from applications.model.course_paper import CoursePaper
from applications.model.stage import Stage
from applications.model.stages import Stages
# from applications.repository.mapper import course_paper_to_model, model_to_course_paper

import sqlite3

class CoursePaperRepository:
    def create(self, course_paper: CoursePaper) -> None:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO CoursePaperModel (
                course_paper_id, 
                course_paper_name, 
                course_paper_student_id, 
                course_paper_created_at, 
                course_paper_current_stage
            ) VALUES (?, ?, ?, ?, ?)
        """, (course_paper.id, course_paper.name, course_paper.student_id, str(course_paper.created_at), course_paper.current_stage.value))
        conn.commit()
        conn.close()
    
    
    def list(self, limit, offset) -> list[CoursePaper]:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CoursePaperModel LIMIT ? OFFSET ?", (limit, offset))
        rows = cursor.fetchall()
        conn.close()
        return [CoursePaper.from_tuple(row) for row in rows]
    
    
    def update_stage(self, course_paper_id: str, stage: Stages) -> None:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE CoursePaperModel
            SET course_paper_current_stage = ?
            WHERE course_paper_id = ?
        """, (stage, course_paper_id))
        conn.commit()
        conn.close()
        

    def get(self, course_paper_id: str) -> CoursePaper:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CoursePaperModel WHERE course_paper_id = ?", (course_paper_id,))
        row = cursor.fetchone()
        conn.close()
        return CoursePaper.from_tuple(row)
    
    
    def get_count(self) -> int:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM CoursePaperModel
        """)
        count = cursor.fetchone()[0]
        conn.close()
        return count


course_paper_repository = CoursePaperRepository()