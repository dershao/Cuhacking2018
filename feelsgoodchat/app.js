var express = require('express');
var http = require('http');
var socket = require('./socket-events.js');

//initialize express app
var app = express();

//initialize http server
var httpServer = http.Server(app);

//initialize instance of socket by passing http server
var io = require('socket.io')(httpServer);

//set view engine
app.set('view engine', 'ejs');

app.use(express.static("./public"))

app.get('/chat', function(req, res) {

	res.render('index', {room : req.query.room});
});

socket(io);

const port = process.env.PORT || 5000; 

httpServer.listen(port, function() {
	console.log('Listening on port: 5000');
});
