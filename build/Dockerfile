FROM golang:1.15-alpine as reloader

WORKDIR /github.com/abatilo/streamlit-preview-environments-demo
COPY go.mod go.sum ./
RUN go mod download -x

COPY cmd ./cmd
COPY internal ./internal
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go install -ldflags="-w -s" ./...

FROM python:3.8.5-alpine

WORKDIR /github.com/abatilo/streamlit-preview-environments-demo
RUN apk add --no-cache \
      git=2.26.2-r0 \
      gcc=9.3.0-r2 \
      musl-dev=1.1.24-r9 \
      libffi-dev=3.3-r2 \
      openssl=1.1.1g-r0 \
      libressl-dev=3.1.2-r0
RUN pip install poetry==1.0.9

COPY --from=reloader /go/bin/reloader /usr/local/bin/reloader
COPY streamlit-application ./streamlit-application

ENTRYPOINT ["reloader"]
