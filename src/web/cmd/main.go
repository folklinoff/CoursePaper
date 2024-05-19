package main

import (
	"context"
	"flag"
	"log"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/folklinoff/course_paper_frontend/internal"
	"github.com/folklinoff/course_paper_frontend/internal/app"
)

var cfg = flag.String("config", "", "config file path")

func main() {
	flag.Parse()
	appConfig, err := internal.LoadAppConfig(*cfg)
	if err != nil {
		log.Panicf("failed to get app config: %q", err)
	}

	app := app.New(*appConfig)
	applicationErrors := make(chan error)

	go func() {
		applicationErrors <- app.Start()
	}()

	log.Printf("started a server on port %d", appConfig.Port)

	stop := make(chan os.Signal, 1)
	signal.Notify(stop, syscall.SIGTERM, syscall.SIGINT)

	select {
	case err := <-applicationErrors:
		log.Fatalf("error happened while running web server: %s", err.Error())
	case <-stop:
		ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
		defer cancel()
		app.Shutdown(ctx)
	}
}
