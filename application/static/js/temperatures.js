function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function send_request(socket, temperature, timeseries) {
    await sleep(3000);
    socket.send(temperature + '|' + timeseries);
    await sleep(3000);
}

let default_labels = ['0', '1', '2', '3', '4', '5'];
let default_label = 'Температура';
let default_data = [20, 21, 22, 23, 25, 30];
let ctx = document.getElementById('myChart');
window.graphData = {
    type: 'line',
    data: {
        labels: default_labels,
        datasets: [{
            // label: default_label,
            data: default_data,
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

function graphic(value, labels, data) {
    // graphData.data.datasets[0].label = label;
    graphData.data.labels = labels;
    //graphData.data.datasets[0].data = data;

    let new_data = graphData.data.datasets[0].data;
    if (new_data.length > 6) {
        new_data.shift();
        new_data.push(value);
        graphData.data.datasets[0].data = new_data;
    } else {
        graphData.data.datasets[0].data = data;
    }
    myChart.update();
}

let temperature = document.getElementById('uniqueID');
console.log(temperature)

let text = temperature.innerText;
//let currency1 = String(text.slice(0, 3));
console.log(text);
//let currency2 = String(text.slice(4, 7));

let socket = new WebSocket('ws://127.0.0.1:8000/ws/temperatures/');

socket.onmessage = function(event) {
    let server_data = JSON.parse(event.data);
    let x_data = server_data.x;
    let y_data = server_data.y;
    console.log(x_data);
    console.log(y_data);

    let value = server_data.value;

    console.log(typeof text);
    console.log(text);
    if (status == 'connected') {
        console.log('Websocket connected');
        status = 'day';
    } else if (status == 'day') {
        console.log('day');
        graphic(value, x_data, y_data);
    } else if (status == 'hour') {
        console.log('hour');
        graphic(value, x_data, y_data);
    } else if (status == 'halfhour') {
        console.log('halfhour');
        graphic(value, x_data, y_data);
    } else if (status == '10min') {
        console.log('10min');
        graphic(value, x_data, y_data);
    } else {
        console.log('garbage');
    }
    let timeseries = status;

    send_request(socket, temperature, timeseries);
}


socket.onopen = function() {
    console.log('Onopen');
}

socket.onclose = function(event) {
    console.log('Onclose');
}

socket.onerror = function(error) {
    console.log('Ошибка ' + error.message);
}