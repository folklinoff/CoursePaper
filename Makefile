docker.up: docker.build
	docker run -d -p 8000:8000 --name=backend --rm backend
	docker run -d -p 80:80 --name=nginx --rm nginx

docker.build:
	docker build -t backend ./src/backend
	docker build -t nginx ./nginx