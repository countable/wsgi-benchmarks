#!/bin/sh

for server in web bjoern meinheld gaiohttp sanic
do
  echo $server
  ab -c 10 -n 5000  http://$server:8000/  2>&1 | grep "Requests per second"
done

