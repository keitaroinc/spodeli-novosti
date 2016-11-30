VERSION := $(shell git describe --tags --exact-match 2>/dev/null || echo latest)
DOCKERHUB_NAMESPACE ?= keitaro
IMAGE := ${DOCKERHUB_NAMESPACE}/spodelinovosti-api:${VERSION}

build:
	docker build -t ${IMAGE} .

push: build
	docker push ${IMAGE}

test:
	docker run -d --name sn_test_db -p 28115:28015 rethinkdb:2.3.5
	-RDB_PORT=28115 nosetests
	docker stop sn_test_db
	docker rm sn_test_db

coverage:
	docker run -d --name sn_testcover_db -p 28115:28015 rethinkdb:2.3.5
	-rm -rf cover
	-RDB_PORT=28115 nosetests --with-coverage --cover-package=app --cover-html
	docker stop sn_testcover_db
	docker rm sn_testcover_db
