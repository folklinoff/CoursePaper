package models

import (
	"time"
)

type CoursePaper struct {
	ID           string    `json:"id"`
	Name         string    `json:"name"`
	StudentID    string    `json:"student_id"`
	CurrentStage string    `json:"current_stage"`
	CreatedAt    time.Time `json:"created_at"`
}
