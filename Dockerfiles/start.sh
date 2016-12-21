#!/bin/bash

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

sudo docker run -p 2999:3000 -d --name freeboard alexiasa/freeboard
sudo docker run -d --name mongodbdb -p 27017:27017 mongo
sudo docker run -d -p 1883:1883 -p 3000:3000 -p 5683:5683 --name ponte hahaha
sudo docker run -p 1880:1880 -d nodered/node-red-docker


