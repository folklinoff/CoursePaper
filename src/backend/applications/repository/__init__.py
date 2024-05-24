import sqlite3
import uuid
from applications.model.stages import Stages


conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stages (
        stage_name TEXT PRIMARY KEY
    )
""")

stages = [(stage.value,) for stage in Stages]
cursor.executemany("""
    INSERT OR IGNORE INTO Stages (stage_name)
    VALUES (?)
""", stages)
conn.commit()
conn.close()


conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS CoursePaperModel (
        course_paper_id TEXT PRIMARY KEY,
        course_paper_name TEXT NOT NULL,
        course_paper_student_id TEXT NOT NULL,
        course_paper_created_at DATETIME NOT NULL,
        course_paper_current_stage TEXT NOT NULL,
        FOREIGN KEY (course_paper_current_stage) REFERENCES Stages(stage_name) 
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS StageModel (
        stage_id TEXT PRIMARY KEY,
        stage_name TEXT NOT NULL,
        stage_created_at DATETIME NOT NULL,
        stage_course_paper_id TEXT NOT NULL,
        FOREIGN KEY (stage_course_paper_id) REFERENCES CoursePaperModel(course_paper_id)
    );
''')