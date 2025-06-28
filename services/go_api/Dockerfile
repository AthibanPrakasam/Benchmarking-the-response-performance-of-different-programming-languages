FROM golang:1.22

WORKDIR /app

COPY . .

RUN go mod init go-processor
RUN go get github.com/gin-gonic/gin
RUN go mod tidy

RUN go build -o app

EXPOSE 8002

CMD ["./app"]
