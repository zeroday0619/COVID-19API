#!/usr/bin/env sh
cd COVID-19API
git pull
redis-cli FLUSHALL
sudo uvicorn run:app --host 0.0.0.0 --port 443 --ssl-keyfile=./zerodayprivkey.pem --ssl-certfile=zeroday.pem --reload &
disown
exit