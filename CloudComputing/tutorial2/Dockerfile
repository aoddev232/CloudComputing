FROM ubuntu:18.04

LABEL maintainer="tutorial2"

RUN apt-get -y update && apt-get -y install nginx

COPY . /src

EXPOSE 80

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]