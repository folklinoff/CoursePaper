docker.up: docker.build
	docker run -d -p 8000:8000 --name=app --rm app
	docker run -d -p 80:80 --name=nginx --rm nginx

docker.build:
	docker build -t app ./src
	docker build -t nginx ./nginx