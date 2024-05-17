package storage

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"github.com/folklinoff/course_paper_frontend/internal"
	"github.com/folklinoff/course_paper_frontend/internal/storage/dto"
	"github.com/folklinoff/course_paper_frontend/internal/storage/models"
)

const (
	coursePapersPath = "/api/course_papers"
)

type Storage interface {
	GetCoursePapersCount() (int, error)
	GetStagesCount(coursePaperID string) (int, error)
	Get(limit int, offset int) ([]*models.CoursePaper, error)
	Create(createCoursePaper dto.CreateCoursePaperDTO) (*models.CoursePaper, error)
	UpdateStage(coursePaperID string, newStage dto.UpdateStageDTO) (*models.CoursePaper, error)
	ListStages(coursePaperID string, limit int, offset int) ([]*models.Stage, error)
}

type storage struct {
	url string
}

func New(config internal.StorageConfig) Storage {
	return &storage{url: config.URL}
}

func (s *storage) GetCoursePapersCount() (int, error) {
	return s.getCount(s.url + coursePapersPath)
}

func (s *storage) GetStagesCount(coursePaperID string) (int, error) {
	return s.getCount(fmt.Sprintf("%s%s/%s/stages", s.url, coursePapersPath, coursePaperID))
}

func (s *storage) getCount(path string) (int, error) {
	rawBody, err := makeRequest(http.MethodGet, path+":count", "")
	if err != nil {
		return 0, err
	}
	response := make(map[string]int)
	err = json.Unmarshal(rawBody, &response)
	if err != nil {
		return 0, fmt.Errorf("failed to unmarshal backend server response: %w", err)
	}
	return response["count"], nil
}

func (s *storage) Get(limit int, offset int) ([]*models.CoursePaper, error) {
	query := fmt.Sprintf("limit=%d&offset=%d", limit, offset)
	rawBody, err := makeRequest(http.MethodGet, s.url+coursePapersPath+fmt.Sprintf("?%s", query), "")
	if err != nil {
		return nil, err
	}
	response := make(map[string][]*models.CoursePaper)
	err = json.Unmarshal(rawBody, &response)
	if err != nil {
		return nil, fmt.Errorf("failed to unmarshal backend server response: %w", err)
	}
	return response["course_papers"], nil
}

func (s *storage) Create(createCoursePaper dto.CreateCoursePaperDTO) (*models.CoursePaper, error) {
	requestBody, err := json.Marshal(createCoursePaper)
	if err != nil {
		return nil, fmt.Errorf("failed to marshal request body: %w", err)
	}

	rawBody, err := makeRequest(http.MethodPost, s.url+coursePapersPath, string(requestBody))
	if err != nil {
		return nil, err
	}

	var response *models.CoursePaper = &models.CoursePaper{}
	err = json.Unmarshal(rawBody, &response)
	if err != nil {
		return nil, fmt.Errorf("failed to unmarshal backend server response: %w", err)
	}
	return response, nil
}

func (s *storage) UpdateStage(coursePaperID string, newStage dto.UpdateStageDTO) (*models.CoursePaper, error) {
	requestBody, err := json.Marshal(newStage)
	if err != nil {
		return nil, fmt.Errorf("failed to marshal request body: %w", err)
	}

	rawBody, err := makeRequest(http.MethodPost, s.url+fmt.Sprintf("%s/%s/stages", coursePapersPath, coursePaperID), string(requestBody))
	if err != nil {
		return nil, err
	}

	response := &models.CoursePaper{}
	err = json.Unmarshal(rawBody, &response)
	if err != nil {
		return nil, fmt.Errorf("failed to unmarshal backend server response: %w", err)
	}
	return response, nil
}

func (s *storage) ListStages(coursePaperID string, limit int, offset int) ([]*models.Stage, error) {
	query := fmt.Sprintf("limit=%d&offset=%d", limit, offset)
	rawBody, err := makeRequest(http.MethodGet, s.url+fmt.Sprintf("%s/%s/stages?%s", coursePapersPath, coursePaperID, query), "")
	if err != nil {
		return nil, err
	}

	response := make(map[string][]*models.Stage)
	err = json.Unmarshal(rawBody, &response)
	if err != nil {
		return nil, fmt.Errorf("failed to unmarshal backend server response: %w", err)
	}
	return response["stages"], nil
}

func makeRequest(method string, url string, rawRequest string) (rawResponse []byte, err error) {
	var body io.Reader
	if rawRequest != "" {
		body = bytes.NewBufferString(rawRequest)
	}
	request, err := http.NewRequest(method, url, body)
	request.Header.Set("Content-Type", "application/json")
	if err != nil {
		return nil, fmt.Errorf("failed to create request: %w", err)
	}
	client := http.DefaultClient
	resp, err := client.Do(request)
	if err != nil {
		return nil, fmt.Errorf("error happened while making request to backend server: %w", err)
	}
	rawResponse, err = io.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("failed to read server response body: %w", err)
	}
	if 400 <= resp.StatusCode && resp.StatusCode < 500 {
		return nil, fmt.Errorf("incorrect request (status code: %d, response body: %q)", resp.StatusCode, rawResponse)
	}
	if 500 <= resp.StatusCode && resp.StatusCode < 600 {
		return nil, fmt.Errorf("error happened while fetching data (status code: %d, response body: %q)", resp.StatusCode, rawResponse)
	}
	return rawResponse, nil
}
