FROM golang:1.15-alpine as reloader

WORKDIR /github.com/abatilo/streamlit-preview-environments-demo
COPY go.mod go.sum ./
RUN go mod download -x
RUN go get github.com/monzo/envoy-preflight

COPY cmd ./cmd
COPY internal ./internal
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go install -ldflags="-w -s" ./...

FROM python:3.8.5

WORKDIR /github.com/abatilo/streamlit-preview-environments-demo
RUN pip install streamlit==0.67.0

COPY --from=reloader /go/bin/envoy-preflight /usr/local/bin/envoy-preflight
COPY --from=reloader /go/bin/reloader /usr/local/bin/reloader
ENTRYPOINT ["envoy-preflight", "reloader"]
