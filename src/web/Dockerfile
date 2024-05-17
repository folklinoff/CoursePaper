FROM golang AS build

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod tidy

COPY . .

RUN go install github.com/a-h/templ/cmd/templ@latest
RUN templ generate

RUN go build -o main ./cmd/main.go
FROM ubuntu as runner

WORKDIR /app

COPY --from=build /app/main .
CMD [ "./main" ]