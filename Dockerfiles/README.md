## How to Run the Dockerfiles

First of all, download all the docker files and load it to your docker images base.
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
$ sudo docker run -p 3000:3000 alexiasa/freeboard
```
(The freeboard will be on the port 3000 on the localhost)


Also, we can link a container with another by the option `--link`, so Ponte can be directly linked to MongoDB
(but I'm still not able to set a configuration to an existed docker image)

## MongoDB

MongoDB can be run on docker by this command:
```
sudo docker run --name <name-of-db> -d mongo
```

## Where to Store the Data?
