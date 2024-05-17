# Details

Date : 2024-05-15 02:40:14

Directory /Users/folklinoff/Documents/Uni/CoursePaper/course_papers/app

Total : 58 files,  2053 codes, 40 comments, 342 blanks, all 2435 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [.gitlab-ci.yml](/.gitlab-ci.yml) | YAML | 6 | 0 | 2 | 8 |
| [Makefile](/Makefile) | Makefile | 8 | 0 | 3 | 11 |
| [docker-compose.yml](/docker-compose.yml) | YAML | 42 | 0 | 1 | 43 |
| [nginx/.gitlab-ci.yml](/nginx/.gitlab-ci.yml) | YAML | 41 | 0 | 2 | 43 |
| [nginx/Dockerfile](/nginx/Dockerfile) | Docker | 5 | 0 | 2 | 7 |
| [nginx/conf/nginx.conf](/nginx/conf/nginx.conf) | Properties | 10 | 8 | 3 | 21 |
| [src/backend/.gitlab-ci.yml](/src/backend/.gitlab-ci.yml) | YAML | 41 | 0 | 2 | 43 |
| [src/backend/Dockerfile](/src/backend/Dockerfile) | Docker | 13 | 1 | 5 | 19 |
| [src/backend/app_uwsgi.ini](/src/backend/app_uwsgi.ini) | Ini | 6 | 0 | 0 | 6 |
| [src/backend/applications/__init__.py](/src/backend/applications/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [src/backend/applications/admin.py](/src/backend/applications/admin.py) | Python | 4 | 1 | 1 | 6 |
| [src/backend/applications/apps.py](/src/backend/applications/apps.py) | Python | 4 | 0 | 3 | 7 |
| [src/backend/applications/decorators/error_handler.py](/src/backend/applications/decorators/error_handler.py) | Python | 12 | 0 | 2 | 14 |
| [src/backend/applications/migrations/0001_initial.py](/src/backend/applications/migrations/0001_initial.py) | Python | 27 | 1 | 7 | 35 |
| [src/backend/applications/migrations/__init__.py](/src/backend/applications/migrations/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [src/backend/applications/model/course_paper.py](/src/backend/applications/model/course_paper.py) | Python | 10 | 0 | 2 | 12 |
| [src/backend/applications/model/stage.py](/src/backend/applications/model/stage.py) | Python | 10 | 1 | 4 | 15 |
| [src/backend/applications/model/stages.py](/src/backend/applications/model/stages.py) | Python | 8 | 0 | 2 | 10 |
| [src/backend/applications/models.py](/src/backend/applications/models.py) | Python | 13 | 0 | 5 | 18 |
| [src/backend/applications/repository/course_paper.py](/src/backend/applications/repository/course_paper.py) | Python | 20 | 0 | 12 | 32 |
| [src/backend/applications/repository/mapper.py](/src/backend/applications/repository/mapper.py) | Python | 33 | 0 | 8 | 41 |
| [src/backend/applications/repository/stage.py](/src/backend/applications/repository/stage.py) | Python | 12 | 0 | 12 | 24 |
| [src/backend/applications/serializers/course_paper.py](/src/backend/applications/serializers/course_paper.py) | Python | 17 | 0 | 8 | 25 |
| [src/backend/applications/serializers/openapi: 3.yml](/src/backend/applications/serializers/openapi:%203.yml) | YAML | 149 | 0 | 3 | 152 |
| [src/backend/applications/serializers/stage.py](/src/backend/applications/serializers/stage.py) | Python | 14 | 0 | 9 | 23 |
| [src/backend/applications/services/course_paper.py](/src/backend/applications/services/course_paper.py) | Python | 37 | 0 | 17 | 54 |
| [src/backend/applications/tests.py](/src/backend/applications/tests.py) | Python | 1 | 1 | 2 | 4 |
| [src/backend/applications/views.py](/src/backend/applications/views.py) | Python | 86 | 1 | 11 | 98 |
| [src/backend/course_papers/__init__.py](/src/backend/course_papers/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [src/backend/course_papers/asgi.py](/src/backend/course_papers/asgi.py) | Python | 10 | 0 | 7 | 17 |
| [src/backend/course_papers/settings.py](/src/backend/course_papers/settings.py) | Python | 86 | 16 | 35 | 137 |
| [src/backend/course_papers/urls.py](/src/backend/course_papers/urls.py) | Python | 28 | 0 | 3 | 31 |
| [src/backend/course_papers/wsgi.py](/src/backend/course_papers/wsgi.py) | Python | 10 | 0 | 7 | 17 |
| [src/backend/manage.py](/src/backend/manage.py) | Python | 17 | 1 | 5 | 23 |
| [src/backend/requirements.txt](/src/backend/requirements.txt) | pip requirements | 7 | 0 | 0 | 7 |
| [src/web/.gitlab-ci.yml](/src/web/.gitlab-ci.yml) | YAML | 41 | 0 | 2 | 43 |
| [src/web/Dockerfile](/src/web/Dockerfile) | Docker | 12 | 0 | 6 | 18 |
| [src/web/cmd/main.go](/src/web/cmd/main.go) | Go | 36 | 0 | 11 | 47 |
| [src/web/docker-compose.yml](/src/web/docker-compose.yml) | YAML | 10 | 0 | 0 | 10 |
| [src/web/go.mod](/src/web/go.mod) | Go Module File | 21 | 0 | 4 | 25 |
| [src/web/go.sum](/src/web/go.sum) | Go Checksum File | 43 | 0 | 1 | 44 |
| [src/web/internal/app/app.go](/src/web/internal/app/app.go) | Go | 33 | 0 | 10 | 43 |
| [src/web/internal/config.go](/src/web/internal/config.go) | Go | 79 | 0 | 17 | 96 |
| [src/web/internal/handler/course_papers.go](/src/web/internal/handler/course_papers.go) | Go | 69 | 0 | 14 | 83 |
| [src/web/internal/handler/handler.go](/src/web/internal/handler/handler.go) | Go | 20 | 0 | 7 | 27 |
| [src/web/internal/handler/middleware.go](/src/web/internal/handler/middleware.go) | Go | 13 | 0 | 3 | 16 |
| [src/web/internal/storage/dto/course_paper.go](/src/web/internal/storage/dto/course_paper.go) | Go | 5 | 0 | 2 | 7 |
| [src/web/internal/storage/dto/stage.go](/src/web/internal/storage/dto/stage.go) | Go | 4 | 0 | 2 | 6 |
| [src/web/internal/storage/models/course_paper.go](/src/web/internal/storage/models/course_paper.go) | Go | 11 | 0 | 3 | 14 |
| [src/web/internal/storage/models/stage.go](/src/web/internal/storage/models/stage.go) | Go | 8 | 0 | 3 | 11 |
| [src/web/internal/storage/storage.go](/src/web/internal/storage/storage.go) | Go | 131 | 0 | 20 | 151 |
| [src/web/views/course_paper.templ](/src/web/views/course_paper.templ) | templ | 74 | 0 | 8 | 82 |
| [src/web/views/course_paper_templ.go](/src/web/views/course_paper_templ.go) | Go | 279 | 3 | 11 | 293 |
| [src/web/views/index.templ](/src/web/views/index.templ) | templ | 94 | 0 | 7 | 101 |
| [src/web/views/index_templ.go](/src/web/views/index_templ.go) | Go | 193 | 3 | 10 | 206 |
| [src/web/views/params/page_display_params.go](/src/web/views/params/page_display_params.go) | Go | 56 | 0 | 6 | 62 |
| [src/web/views/sidenav.templ](/src/web/views/sidenav.templ) | templ | 6 | 0 | 2 | 8 |
| [src/web/views/sidenav_templ.go](/src/web/views/sidenav_templ.go) | Go | 28 | 3 | 5 | 36 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)