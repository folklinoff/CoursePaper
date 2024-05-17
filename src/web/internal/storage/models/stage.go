package models

import "time"

type Stage struct {
	ID          string
	Name        string
	CoursePaper CoursePaper
	CreatedAt   time.Time
}
