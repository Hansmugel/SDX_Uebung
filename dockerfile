#1 stage
#parent image
FROM golang:1.22-alpine AS builder
WORKDIR /src
COPY ./src .
RUN go mod download && \
    go build -o /main

#2 stage
FROM alpine:3.19
COPY --from=builder /main /recipe
RUN adduser -D uebung && chown -R uebung /recipe
USER uebung
ENTRYPOINT ["/recipe"]
CMD ["serve"]
