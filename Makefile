docker.up: docker.build
	docker run -d -p 8000:8000 --name=backend --net=course_papers --hostname=backend backend
	docker run -d -p 80:80 --name=proxy --net=course_papers proxy

docker.build:
	docker build -t backend ./src/backend
	docker build -t proxy ./nginx


web:
	cd ./src/web && templ generate
	cd src/web/ && go run ./cmd --config ./.env


db:
	cd src/backend && \
		rm -f db.sqlite3 && \
		python3 manage.py migrate
	