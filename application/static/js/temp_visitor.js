let DATA_GRAPH = [0, 0, 0, 0, 0, 0]

const NUMBER_POINTS = 6



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

const QueryString = window.location.pathname
console.log(QueryString)
console.log(typeof QueryString)
let q = QueryString.split("/")
console.log(q)
let id = q[q.length - 1]
console.log(id)
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

let timeseries = 0;
let data = 20;

socket.onmessage = function(event) {
    let server_data = JSON.parse(event.data)
    let temperature = server_data.temperature
    let current_temp = server_data.current_temp

    console.log(server_data)
    for (let i = 0; i < NUMBER_POINTS; i++) {
        DATA_GRAPH[i] = temperature[i]
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

setInterval(global, 1000)