const net = require('node:net');

var client = new net.Socket();
client.connect(5000, '127.0.0.1', function() {
    console.log('Connected');
    client.write('teszt');

});
