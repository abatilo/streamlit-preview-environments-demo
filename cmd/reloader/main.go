package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"

	"github.com/abatilo/streamlit-preview-environments-demo/internal/logger"
	"github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/plumbing"
	"github.com/kelseyhightower/envconfig"
)

// Configuration represents the environment variables which are used to configure the reloader application
type Configuration struct {
	Repo      string
	Directory string // Relative to root of cloned repo
	Branch    string
}

func main() {
	log := logger.NewLogger()

	var cfg Configuration
	err := envconfig.Process("reloader", &cfg)
	if err != nil {
		log.Error(err, "could not process config")
		os.Exit(1)
	}

	if cfg.Repo == "" {
		log.Error(fmt.Errorf("RELOADER_REPO is a required environment variable"), "missing config")
		os.Exit(1)
	}

	if cfg.Directory == "" {
		log.Info("Using default directory of \".\"")
		cfg.Directory = "."
	}

	if cfg.Branch == "" {
		log.Info("Using default branch of \"master\"")
		cfg.Branch = "master"
	}

	cloneDir, _ := ioutil.TempDir("", "cloned-*")
	branchName := plumbing.ReferenceName(fmt.Sprintf("refs/heads/%s", cfg.Branch))

	log.Info("Cloning to " + cloneDir)
	repo, err := git.PlainClone(cloneDir, false, &git.CloneOptions{
		Progress:      log,
		URL:           cfg.Directory,
		ReferenceName: branchName,
	})
	if err != nil {
		log.Error(err, "could not clone repo")
		os.Exit(1)
	}

	r := http.NewServeMux()
	r.HandleFunc("/pull", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
			return
		}

		tree, err := repo.Worktree()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		err = tree.Pull(&git.PullOptions{
			Progress:      log,
			ReferenceName: branchName,
		})
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
	})

	srv := &http.Server{
		Addr:    ":8080",
		Handler: r,
	}

	// Run streamlit command
	installCmd := exec.Command("poetry", "install")
	installCmd.Dir = cfg.Directory
	installCmd.Stdout = log
	installCmd.Stderr = log
	installCmd.Run()

	streamlitCmd := exec.Command("poetry", "run", "streamlit", "run", "--server.runOnSave", "true", "main.py")
	streamlitCmd.Dir = cfg.Directory
	streamlitCmd.Stdout = log
	streamlitCmd.Stderr = log
	go streamlitCmd.Run()

	log.Info("Listening...")
	srv.ListenAndServe()
}
