VERSION := $(shell git describe --tags --exact-match 2>/dev/null || echo latest)
DOCKERHUB_NAMESPACE ?= keitaro
IMAGE := ${DOCKERHUB_NAMESPACE}/spodelinovosti-worker:${VERSION}

build:
	docker build -t ${IMAGE} .

push: build
	docker push ${IMAGE}