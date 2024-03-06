FROM python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /d/app_

COPY ./req.txt /d/app_
RUN pop install -r 
LABEL authors="olezk"

ENTRYPOINT ["top", "-b"]