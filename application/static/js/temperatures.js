let connectionString = 'ws://' + window.location.host + '/ws/temperatures/'
let socket = new WebSocket(connectionString)

function send_request(socket, text_data) {
    socket.send(text_data)
}

socket.onopen = function() {
    console.log('WS open')
    send_request(socket, {'status': 'OK'})

}

socket.onclose = function(event) {
    console.log('WS close')
}

socket.onmessage = function(event) {
    let server_data = JSON.parse(event.data)
    console.log(server_data)
}

socket.onerror = function(error) {
    console.log('Error ' + error.message)
}

