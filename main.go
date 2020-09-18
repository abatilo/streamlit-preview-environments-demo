package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"

	"github.com/go-chi/chi"
	"github.com/go-git/go-git/v5"
	"github.com/rs/zerolog"
)

// Logger is a wrapper logger around zerolog
type Logger struct {
	logger zerolog.Logger
}

func (l *Logger) Write(p []byte) (n int, err error) {
	l.logger.Info().Msg(string(p))
	return len(p), nil
}

// Info writes a string at info level
func (l *Logger) Info(msg string) {
	l.logger.Info().Msg(msg)
}

// NewLogger creates a wrapped internal logger
func NewLogger() *Logger {
	return &Logger{
		logger: zerolog.New(os.Stdout),
	}
}

func main() {
	log := NewLogger()
	r := chi.NewRouter()

	tempDir, _ := ioutil.TempDir("", "*")

	r.Get("/clone", func(w http.ResponseWriter, r *http.Request) {
		ctx := r.Context()
		log.Info("Cloning to " + tempDir)
		git.PlainCloneContext(ctx, tempDir, false, &git.CloneOptions{
			URL:      "https://www.github.com/abatilo/blog",
			Progress: log,
		})
	})
	r.Get("/pull", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "hello world")
	})
	srv := &http.Server{
		Addr:    ":8080",
		Handler: r,
	}

	log.Info("Listening...")
	srv.ListenAndServe()
}
