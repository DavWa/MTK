module.exports = {
  persistence: {
    // same as http://mcollina.github.io/mosca/docs/lib/persistence/mongo.js.html
    type: "mongo",
    url: "mongodb://<Your_IP_Address>:27017/ponte"
  },
  broker: {
    // same as https://github.com/mcollina/ascoltatori#mongodb
    type: "mongo",
    url: "mongodb://<Your_IP_Address>:27017/ponte"
  },
  logger: {
    level: 30, // or 20 or 40
    name: "MongoPonte"
  }
};
