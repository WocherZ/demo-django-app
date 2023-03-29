let DATA_GRAPH = [20, 21, 22, 24, 27, 30]

//function sleep(ms) {
//    return new Promise(resolve => setTimeout(resolve, ms));
//}

let default_labels = ['0', '1', '2', '3', '4', '5'];
let default_label = 'Температура';
let ctx = document.getElementById('myChart');
window.graphData = {
    type: 'line',
    data: {
        labels: default_labels,
        datasets: [{
            label: default_label,
            data: DATA_GRAPH,
            backgroundColor: [
                'rgba(73, 198, 230, 0.5)',
            ],
            borderWidth: 1,
            borderColor: 'rgb(75, 192, 192)',
            fill: false,
            tension: 0,
        }]
    },
    options: {
        legend: {
            display: false
        },
        scales: {
            x: {
                color: '#87CEEB',
                grid: {
                    display: true,
                    drawBorder: true,
                    drawOnChart: true,
                    drawTicks: true,
                }
            },
            y: {
                color: '##87CEEB',
                grid: {
                    display: true,
                    drawBorder: true,
                    drawOnChart: true,
                    drawTicks: true,
                },
            },
        }
    },
}

let myChart = new Chart(ctx, graphData);

function graphic() {
    graphData.data.datasets[0].data = DATA_GRAPH;
    myChart.update();
}

let connectionString = 'ws://' + window.location.host + '/ws/temperatures/'
let socket = new WebSocket(connectionString)

function send_request(socket, text_data) {
    socket.send(text_data)
}

socket.onopen = function() {
    console.log('WS open')
}

socket.onclose = function(event) {
    console.log('WS close')
}

let timeseries = 0;
let data = 20;

socket.onmessage = function(event) {
    let server_data = JSON.parse(event.data)
    for (let i = 0; i < 6; i++) {
        DATA_GRAPH[i] = DATA_GRAPH[i] + 1
    }
    data = 25
}

socket.onerror = function(error) {
    console.log('Error ' + error.message)
}

function global() {
    send_request(socket, {'status': 'OK'})
    graphic()
}

setInterval(global, 1000)