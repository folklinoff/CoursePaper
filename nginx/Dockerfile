FROM nginx:latest

ARG BACKEND_HOST_IP

RUN apt update && apt-get install -y gettext
COPY ./conf/nginx.conf /etc/nginx/conf.d/default.conf
RUN envsubst < /etc/nginx/conf.d/default.conf > /tmp/conf.txt && cat /tmp/conf.txt > /etc/nginx/conf.d/default.conf && rm /tmp/conf.txt