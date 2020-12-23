FROM python:3.6-alpine

ARG APP_USER=app
ARG APP_DIR=web

ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/$APP_USER/$APP_DIR

RUN apk upgrade --update
WORKDIR $APP_HOME

RUN adduser -D $APP_USER
RUN chown -R $APP_USER:$APP_USER $APP_HOME

RUN apk update \
    && apk add --no-cache gettext openssh-client git gcc zlib-dev jpeg-dev python3-dev musl-dev libressl-dev libffi-dev \
    && pip install --upgrade pip

COPY demo/requirements.txt .
RUN pip install -r requirements.txt
COPY --chown=$APP_USER:$APP_USER . $APP_HOME
RUN pip install -e .

USER $APP_USER