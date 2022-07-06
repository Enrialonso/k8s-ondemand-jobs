IMAGE_NAME_API=flask-api
IMAGE_NAME_JOB=python-job

build:
	docker build -f ./api/Dockerfile -t $(IMAGE_NAME_API) ./api
	docker build -f ./job/Dockerfile -t $(IMAGE_NAME_JOB) ./job

deploy:
	make build
	kubectl apply -f ./api

remove:
	kubectl delete -f ./api
