package app

import (
	"context"
	"fmt"
	"net/http"

	"github.com/folklinoff/course_paper_frontend/internal"
	"github.com/folklinoff/course_paper_frontend/internal/handler"
	"github.com/folklinoff/course_paper_frontend/internal/storage"
)

type App struct {
	Host string
	Port int

	srv *http.Server

	Storage storage.Storage
}

func New(config internal.AppConfig) *App {
	storage := storage.New(config.DataSourceConfig)
	return &App{
		Host: config.Host,
		Port: config.Port,

		Storage: storage,
	}
}

func (a *App) Start() error {
	a.srv = &http.Server{
		Addr:    fmt.Sprintf(":%d", a.Port),
		Handler: handler.New(a.Storage),
	}
	return a.srv.ListenAndServe()
}

func (a *App) Shutdown(ctx context.Context) {
	_ = a.srv.Shutdown(ctx)
}
