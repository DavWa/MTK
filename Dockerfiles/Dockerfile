FROM ubuntu
ADD config.js .
RUN apt-get update && apt-get install curl nano -y
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash
RUN apt-get install nodejs -y
RUN npm install bunyan ponte -g
RUN npm install express
RUN npm install ponte --save
RUN npm install socket.io
CMD ponte -c config.js
