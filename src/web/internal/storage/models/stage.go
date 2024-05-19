package models

import "time"

type Stage struct {
	ID          string    `json:"id"`
	Name        string    `json:"name"`
	CoursePaper string    `json:"course_paper_id"`
	CreatedAt   time.Time `json:"created_at"`
}
