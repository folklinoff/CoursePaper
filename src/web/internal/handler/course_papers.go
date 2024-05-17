package handler

import (
	"fmt"
	"net/http"

	"github.com/folklinoff/course_paper_frontend/internal/storage"
	"github.com/folklinoff/course_paper_frontend/internal/storage/dto"
	"github.com/folklinoff/course_paper_frontend/views"
	"github.com/folklinoff/course_paper_frontend/views/course_papers"
	"github.com/folklinoff/course_paper_frontend/views/params"
	"github.com/folklinoff/course_paper_frontend/views/stages"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	humanlog "github.com/tiramiseb/echo-humanlog"
)

type CoursePaperHandler struct {
	storage storage.Storage
}

func NewCoursePaperHandler(storage storage.Storage) *CoursePaperHandler {
	return &CoursePaperHandler{
		storage: storage,
	}
}

func (h *CoursePaperHandler) Register(e *echo.Echo) {
	e.Logger.SetOutput(humanlog.New(e.Logger.Output()))
	e.Use(middleware.LoggerWithConfig(LoggerConfig))
	e.Use(middleware.Logger())
	e.GET("/", echo.HandlerFunc(h.Index), RedirectWithQueryParams)
	e.GET("/course_papers", echo.HandlerFunc(h.Get), RedirectWithQueryParams)
	e.POST("/course_papers", echo.HandlerFunc(h.Post))
	e.GET("/course_papers/:id/stages", echo.HandlerFunc(h.ListStages), RedirectWithQueryParams)
	e.POST("/course_papers/:id/stages", echo.HandlerFunc(h.UpdateStage))
}

func (h *CoursePaperHandler) Index(c echo.Context) error {
	params, err := params.GetPageDisplayParams(c.QueryParams())
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get display params: %w", err))
	}

	coursePapers, err := h.storage.Get(params.Limit, params.Limit*(params.CurrentPage-1))
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get course papers: %w", err))
	}

	coursePapersCount, err := h.storage.GetCoursePapersCount()
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get course papers count: %w", err))
	}

	c.Response().Header().Set("Content-Type", "text/html")
	err = views.Index(
		course_papers.Body(
			course_papers.TableWithPagination(
				coursePapers,
				coursePapersCount,
				params,
			),
		)).
		Render(c.Request().Context(), c.Response().Writer)
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get course papers: %w", err))
	}
	return nil
}

func (h *CoursePaperHandler) Get(c echo.Context) error {
	params, err := params.GetPageDisplayParams(c.QueryParams())
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get display params: %w", err))
	}

	coursePapers, err := h.storage.Get(params.Limit, params.Limit*(params.CurrentPage-1))
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get course papers: %w", err))
	}

	coursePapersCount, err := h.storage.GetCoursePapersCount()
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get course papers count: %w", err))
	}

	c.Response().Header().Set("Content-Type", "text/html")
	err = course_papers.TableWithPagination(coursePapers, coursePapersCount, params).Render(c.Request().Context(), c.Response().Writer)
	if err != nil {
		return echo.NewHTTPError(http.StatusInternalServerError, err)
	}
	return nil
}

func (h *CoursePaperHandler) Post(c echo.Context) error {
	request := dto.CreateCoursePaperDTO{}
	if err := c.Bind(&request); err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to unmarshal request: %w", err))
	}
	c.Response().Header().Set("Content-Type", "text/html")
	coursePaper, err := h.storage.Create(request)
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to create course paper: %w", err).Error())
	}
	err = course_papers.CoursePaperTemplate(*coursePaper).Render(c.Request().Context(), c.Response().Writer)
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get course papers: %w", err))
	}
	return nil
}

func (h *CoursePaperHandler) ListStages(c echo.Context) error {
	params, err := params.GetPageDisplayParams(c.QueryParams())
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get display params: %w", err))
	}

	stagesList, err := h.storage.ListStages(c.Param("id"), params.Limit, params.Limit*(params.CurrentPage-1))
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get course papers: %w", err))
	}

	stagesCount, err := h.storage.GetStagesCount(c.Param("id"))
	if err != nil {
		return echo.NewHTTPError(http.StatusBadRequest, fmt.Errorf("failed to get course papers count: %w", err))
	}

	c.Response().Header().Set("Content-Type", "text/html")
	err = stages.Body(
		stages.TableWithPagination(
			stagesList,
			stagesCount,
			params,
		),
	).Render(c.Request().Context(), c.Response().Writer)
	if err != nil {
		return echo.NewHTTPError(http.StatusInternalServerError, err)
	}
	return nil
}

func (h *CoursePaperHandler) UpdateStage(c echo.Context) error {
	return nil
}
