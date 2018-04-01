
//create a private chat room with socket

module.exports = function(io) {

	users = [];

	//var nsp = io.of('/chat');

	//nsp.on
	io.on('connection', function(socket) {

		//3. increments number of users and join room, emit to everyone that someone has joined
		socket.on('join room', function(data) {

			//if user is not unique, keep increment id
			while (users.indexOf(data.user) > 0) {
				data.user = data.user + 1;
			}
			socket.join(data.room);
			io.sockets.in(data.room).emit('join', data.user);
		});

		socket.on('new message', function(data) {

		 	io.sockets.in(data.room).emit('chat message', data.msg);
		});	

		socket.on('disconnect', function() {
			console.log("A user  has disconnected");
			socket.emit('chat message', "A user has disconnected");
		});
	});
}