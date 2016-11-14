# MTK

## The materials We need

Ponte, Mongodb, Freeboard, sample code for IoT device(in this project we'll take MTK Linkit Smart 7688 Duo as an example).The installation of Ponte and Freeboard will be introduced in this document (MongoDB can be downloaded from [here](https://www.mongodb.com/download-center)). You can also take [Node-Red](https://nodered.org/) as a rule machine if it's necessary.

## Links You may Need

[Ponte Project](https://github.com/eclipse/ponte), [Freeboard/freeboard](https://github.com/Freeboard/freeboard), [MongoDB](https://www.mongodb.com/download-center), [Node-Red](https://nodered.org/).
The docker image files can be found under this repository as well.

## Installation of Ponte

Ponte is a node.js application, so it needs [node.js](http://nodejs.org)
to run. The currently recommended version is node 4.3.1, which is the Longtime Support Version. Ponte is tested against versions 0.12, 4.3.1 and 5. *Attention: you should currently not use ponte with node 5.7*

```
$ npm install ponte bunyan -g
$ ponte -v | bunyan
```
## Configuration


### Configuration with MongoDB

__Ponte__ can be run on top of MongoDB with the following configuration:

```js
module.exports = {
  persistence: {
    // same as http://mcollina.github.io/mosca/docs/lib/persistence/mongo.js.html
    type: "mongo",
    url: "mongodb://localhost:27017/ponte"
  },
  broker: {
    // same as https://github.com/mcollina/ascoltatori#mongodb
    type: "mongo",
    url: "mongodb://localhost:27017/ponte"
  },
  logger: {
    level: 30, // or 20 or 40
    name: "MongoPonte"
  }
};
```

Launch it with `$ ponte -c config.js`.

We can then found a database named ponte in mongodb which saved all the data with the tag "retain=True" for ponte broker.

For a further look of Ponte you can visit [Ponte A](http://www.eclipse.org/ponte/) or the [Ponte Project](https://github.com/eclipse/ponte).





## Freeboard

Freeboard is a turn-key HTML-based "engine" for dashboards.


## How to Use 

Freeboard can be run entirely from a local hard drive by simply download/clone the repository and open index.html.
```
git clone https://github.com/Freeboard/freeboard.git
```

( For more details of freeboard you can visit [Freeboard.io](https://freeboard.io/) or [Freeboard/freeboard](https://github.com/Freeboard/freeboard) )

A sample dashboard can be found in the Freeboard folder.


## Sample code on Iot devices

In this project, there are four sample codes that can be run on the device. All of which( blink.py, temperature.py, humidity.py, pressure.py ) can be found in this folder. By downloading and running these codes, the device will send mqtt message to a remote Ponte broker (on 210.65.89.177). Note that the ponte should always be run before the mqtt message is sent.


## Steps

Here are the steps to connect all these tools into a local monitor for IoT device:


1. Installed Ponte and MongoDB, and copy the config.js file which is shown above.
''
2. If you are under Windows system, then open the MongoDB port is necessary. Run command `$ mongod` under the directory where you have installed your mongoDB. Mostly the directory will be default as C:\Program Files\MongoDB\Server\3.2\.

3. Run Ponte with the configuration with MongoDB
`
$ ponte -c config.js
`

4. Start to send mqtt message to Ponte broker by executing the following python code:
``
$ python blink.py & python temperature.py & python humidity.py & python pressure.py
``
Note that in this sample we take 210.65.89.177 as the host for the ponte broker. You may want to change the host to your own machine(localhost). If you do change the host machine, make sure you have the mqtt connection part modified in each codes. 

5. Setup the local freeboard (steps can be found in the folder of freeboard)


## Check the Persistence Data
(The following instructions are for user under Windows system)

1. Move to the directory where you have installed MongoDB (mostly it will be C:\Program Files\MongoDB\Server\3.2\).

2. Start the MongoDB by running the command `$ mongod`.

3. Start the MongoDB client by running the command `$ mongo` under the same directory.

4. Run the following commands and you will be able to check the received data on Ponte.
```
$ use ponte
$ db.retained.find()
```

