FROM python:3.6.5-jessie

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y apt-file
RUN apt-file update
RUN apt-get install -y nano

RUN echo 'alias ll="ls -alF"' >> ~/.bashrc

RUN mkdir -p /usr/src/app
RUN pip install django==2.0.2 graphene==2.0.1 graphene-django==2.0.0 django-filter==1.1.0 django-graphql-jwt==0.1.5
WORKDIR /usr/src/app