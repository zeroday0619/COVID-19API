FROM ubuntu:bionic
LABEL maintainer="zeroday0619 [Euiseo Cha]"
RUN apt-get update & apt-get upgrade -y
RUN apt-get install python3.8 -y
RUN apt-get install redis-server -y
RUN systemctl enable redis-server.service
RUN python3.8 -m pip install -r requirements.txt
RUN mkdir -p /usr/src/ncov
COPY . /usr/src/ncov
WORKDIR /usr/src/ncov
EXPOSE 80
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "run:app"]