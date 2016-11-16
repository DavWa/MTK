## How to Run the Docker images

First of all, download all the docker files and load it to your docker images base by the command below.
```
$ sudo docker load --input <filename>
```

For Ponte and Freeboard, binding the container port to the localhost is necessary. So we should run the images in this way:

Ponte:
```
$ sudo docker run -p 1883:1883 -p 3000:3000 -p 5683:5683 feverra/ponte
```

Freeboard:
```
$ sudo docker run -p 2999:3000 alexiasa/freeboard
```
Note that the port on the localhost may already be used by other applications (e.g. by Ponte), we may need to bind the freeboard container port to another local system port (2999, for instance, in this example. The freeboard will then be on port 2999 on the localhost).


Also, we can link a container with another by the option `--link`, so Ponte can be directly linked to MongoDB

## MongoDB

MongoDB can be run on docker by this command:
```
$ sudo docker run --name <name-of-db> -d mongo
```
This image includes `EXPOSE 27017` (the mongo port), so if using the mongo client we should bind the container port to the local one as well

```
$ sudo docker run --name <name-of-db> -p 27017:27017 -d mongo
```

## Run Ponte with MongoDB

As mentioned previously, we could use the option `--link` to link two or more containers. In this case, after we've already run MongoDB, we could use the following command for Ponte:
```
$ sudo docker run --link <name-of-fb>:mongo -p 1883:1883 -p 3000:3000 -p 5683:5683 -d feverra/ponte 
```

## Create a docker image for Ponte

Although we can run Ponte and MongoDB simultaneously by following the instructions above, we can't make MongoDB backup the data still. This is because we haven't set the configuration for Ponte to make it "run on MongoDB". However, the existing Ponte docker images is not 
able to do so. Thus, we need to build a docker image for our own.

1. Download the Dockerfile and config.js in this folder.

2. Check the IP address of your machine and modify the content of config.js

3. Put this two file in a same folder.

4. Move to the folder and build your own docker image wtith following command
```
$ sudo docker build -t <the_image name> .
```

After the docker image is built, you can run it on docker in the same way as you run Ponte. This Ponte image will be able to keep data persistence with the help of MongoDB and all the persisted data could be found in Mongo.

## Where to Store the Data?

We can create a directory for Mongo's data storage 
1. Create a data directory on a suitable volume on your host system, e.g. `/my/own/datadir`.
2. Start your `mongo` container like this:
```
$ docker run --name <name-of-db> -v /my/own/datadir:/data/db -d mongo:tag
```
The `-v /my/own/datadir:/data/db` part of the command mounts the `/my/own/datadir` directory from the underlying host system as `/data/db` inside the container, where MongoDB by default will write its data files.
