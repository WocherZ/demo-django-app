let DATA_GRAPH = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
let LABELS_GRAPH = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
let period = 0;

let temp_history = '{{ temp_history }}';

let NUMBER_POINTS = "30"

let visitor_id = document.getElementById("visitor_id").textContent

var button1 = document.getElementById('button1');
var button2 = document.getElementById('button2');
var button3 = document.getElementById('button3');

button1.onclick = function(){
    period = 1;
    NUMBER_POINTS = "30";

}

button2.onclick = function(){
    period = 5;
    NUMBER_POINTS = "150";
}

button3.onclick = function(){
    period = 10;
    NUMBER_POINTS = "300";
}

let DATA_GRAPH = temp_history[:NUMBER_POINTS]

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
let myChart2 = new Chart(ctx, graphData);

function graphic() {
    graphData.data.datasets[0].data = DATA_GRAPH;
    graphData.data.labels = LABELS_GRAPH;
    myChart.update();
}

graphic()
