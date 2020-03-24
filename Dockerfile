FROM matthewfeickert/docker-python3-ubuntu
LABEL maintainer="zeroday0619 [Euiseo Cha]"
RUN sudo apt-get update -y
RUN sudo apt-get upgrade -y
RUN sudo apt-get install python3-pip -y
RUN sudo apt-get install redis-server -y
RUN python3.8 -m pip install fastapi[all] aiohttp[speedup] bs4[speedup] fastapi_plugins scrapy aioredis ujson lxml
RUN mkdir -p /usr/src/ncov
COPY . /usr/src/ncov
WORKDIR /usr/src/ncov
EXPOSE 80
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "run:app"]