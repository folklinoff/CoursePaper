package internal

import (
	"fmt"
	"net/url"
	"os"
	"strconv"

	"github.com/joho/godotenv"

	"golang.org/x/xerrors"
)

type StorageConfig struct {
	URL string
}

type AppConfig struct {
	Host string
	Port int

	DataSourceConfig StorageConfig
}

func LoadAppConfig(filepath string) (*AppConfig, error) {
	if err := loadEnvFile(filepath); err != nil {
		return nil, err
	}

	port, err := loadIntEnv("APP_PORT", 8080)
	if err != nil {
		return nil, err
	}

	sourceConfig, err := loadSourceConfig()
	if err != nil {
		return nil, fmt.Errorf("failed to load source config: %w", err)
	}

	return &AppConfig{
		Host: loadStringEnv("APP_HOST", "localhost"),
		Port: port,

		DataSourceConfig: *sourceConfig,
	}, nil
}

func loadSourceConfig() (*StorageConfig, error) {
	url, err := loadURLEnv("BACKEND_HOST_IP", "")
	if err != nil {
		return nil, fmt.Errorf("failed to load source url: %w", err)
	}
	return &StorageConfig{URL: fmt.Sprintf("http://" + url)}, nil
}

func loadStringEnv(key string, fallback string) string {
	strVal, ok := os.LookupEnv(key)
	if !ok {
		return fallback
	}
	return strVal
}

func loadIntEnv(key string, fallback int) (int, error) {
	strVal, ok := os.LookupEnv(key)
	if !ok {
		return fallback, nil
	}
	val, err := strconv.ParseInt(strVal, 10, 0)
	if err != nil {
		return 0, fmt.Errorf("couldn't parse string %q as int: %w", strVal, err)
	}
	return int(val), nil
}

func loadURLEnv(key string, fallback string) (string, error) {
	strVal, ok := os.LookupEnv(key)
	if !ok {
		return fallback, nil
	}
	if _, err := url.Parse(strVal); err != nil {
		return "", fmt.Errorf("couldn't parse value %q as url: %w", strVal, err)
	}
	return strVal, nil
}

func loadEnvFile(envFilename string) error {
	if envFilename == "" {
		return nil
	}
	if err := godotenv.Load(envFilename); err != nil {
		return xerrors.Errorf("error loading .env file with name %s: %w", envFilename, err)
	}
	return nil
}
