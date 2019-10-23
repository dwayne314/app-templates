FROM python:3.6-alpine

COPY . /opt
WORKDIR /opt

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev bash curl gnupg && \
    apk add postgresql-dev && \
    apk add --update nodejs nodejs-npm && \
	apk add --no-cache wkhtmltopdf


COPY requirements.txt /tmp

RUN pip install --requirement /tmp/requirements.txt


EXPOSE 5000

RUN chmod +x boot.sh
COPY boot.sh /tmp

ENTRYPOINT [ "/tmp/boot.sh" ]

