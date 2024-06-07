From alpine:latest

RUN apk add --no-cache curl

VOLUME /data

COPY config.txt /app/config.txt

CMD ["sh", "-c", "echo 'Hello, Docker Volumes!' > /data/hello.txt && cat /data/hello.txt"]
