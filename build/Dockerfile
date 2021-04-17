FROM golang:1.15-alpine as reloader

WORKDIR /github.com/abatilo/streamlit-preview-environments-demo
COPY go.mod go.sum ./
RUN go mod download -x

COPY cmd ./cmd
COPY internal ./internal
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go install -ldflags="-w -s" ./...

FROM python:3.8.5-slim-buster

WORKDIR /github.com/abatilo/streamlit-preview-environments-demo
RUN pip install streamlit==0.67.0

COPY --from=reloader /go/bin/reloader /usr/local/bin/reloader
ENTRYPOINT ["reloader"]
