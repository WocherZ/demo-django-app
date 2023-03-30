let DATA_GRAPH = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
let LABELS_GRAPH = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
let period = 0;

const NUMBER_POINTS = 12

var button1 = document.getElementById('button1');
var button2 = document.getElementById('button2');
var button3 = document.getElementById('button3');

button1.onclick = function(){
    period = 1;
}

button2.onclick = function(){
    period = 5;
}

button3.onclick = function(){
    period = 10;
}

let default_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'];
let default_label = 'Температура';
let ctx = document.getElementById('myChart');
window.graphData = {
    type: 'line',
    data: {
        labels: LABELS_GRAPH,
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
    graphData.data.lables = LABELS_GRAPH;
    myChart.update();
}

const QueryString = window.location.pathname
let q = QueryString.split("/")
let id = q[q.length - 1]

let connectionString = 'ws://' + window.location.host + '/ws/temp_visitor/' + id + '/'
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


socket.onmessage = function(event) {
    let server_data = JSON.parse(event.data)
    let temperature = server_data.temperature
    let current_temp = server_data.current_temp
    let timeseries = server_data.timeseries

    console.log(timeseries)
    for (let i = 0; i < NUMBER_POINTS; i++) {

        DATA_GRAPH[i] = temperature[i]
        LABELS_GRAPH[i] = timeseries[i]
    }

    document.getElementById("temp_value").textContent=current_temp
}

socket.onerror = function(error) {
    console.log('Error ' + error.message)
}

function global() {
    send_request(socket, {'status': 'OK'})
    graphic()
}

setInterval(global, 2000)