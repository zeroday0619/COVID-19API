FROM python:3.8-alpine
LABEL maintainer="zeroday0619 [Euiseo Cha]"
RUN apk add --no-cache --virtual alpine-sdk build-base python3.8-dev
RUN python3.8 -m pip install fastapi[all] fastapi-plugins
RUN mkdir -p /usr/src/ncov
COPY . /usr/src/ncov
WORKDIR /usr/src/ncov
EXPOSE 80
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "run:app"]