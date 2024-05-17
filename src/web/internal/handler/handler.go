package handler

import (
	"net/http"

	"github.com/folklinoff/course_paper_frontend/internal/storage"
	echo "github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

type Handler struct {
	e *echo.Echo
}

func (h *Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	h.e.ServeHTTP(w, r)
}

func New(storage storage.Storage) *Handler {
	h := &Handler{
		e: echo.New(),
	}
	coursePaperHandler := NewCoursePaperHandler(storage)
	coursePaperHandler.Register(h.e)

	return h
}

var (
	// LoggerConfig is a human-readable log format for the Echo Logger middleware
	LoggerConfig = middleware.LoggerConfig{
		Format: "${time_rfc3339} [ HTTP] \"${method} ${uri}\" ${status} (in: ${bytes_in}, out: ${bytes_out}, latency: ${latency_human})\n",
	}
)
