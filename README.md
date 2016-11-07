# MTK

## Installation

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
