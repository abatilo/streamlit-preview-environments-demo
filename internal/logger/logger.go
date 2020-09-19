// Package logger wraps the zerolog interface
package logger

import (
	"os"

	"github.com/rs/zerolog"
)

// Logger is a wrapper logger around zerolog
type Logger struct {
	logger zerolog.Logger
}

// NewLogger creates a wrapped internal logger
func NewLogger() *Logger {
	return &Logger{
		logger: zerolog.New(os.Stdout).With().Timestamp().Caller().Logger(),
	}
}

// Write is implemented so that we can redirect stdout messages in our usual json log format
func (l *Logger) Write(p []byte) (n int, err error) {
	l.logger.Info().Msg(string(p))
	return len(p), nil
}

// Info writes a string at info level
func (l *Logger) Info(msg string) {
	l.logger.Info().Msg(msg)
}

// Error prints an error message
func (l *Logger) Error(err error, msg string) {
	l.logger.Err(err).Msg(msg)
}
