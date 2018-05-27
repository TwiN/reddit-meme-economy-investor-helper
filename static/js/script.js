$(function () {
    refreshChart();
    setInterval(refreshChart, 5000);
    $.getJSON('/target', function (data) {
        $("#current-target").val(data);
    });
});


function refreshChart() {
    $.getJSON('/scores', function (data) {
        console.log(data);
        $("#data").html(JSON.stringify(data));
        let keys = [], values = [];
        for (let k in data) {
            keys.push(k);
            values.push(data[k]);
        }
        generateChart(keys, values)
    });
}


function generateChart(keys, values) {
    new Chart(document.getElementById("bar-chart"), {
        type: 'line',
        data: {
            labels: keys,
            datasets: [{
                label: "Score",
                data: values
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: 'Score for targeted post'
            },
            bezierCurve: false, // no curvy lines
            xAxes: [{
                type: 'time',
                ticks: {
                    autoSkip: true,
                    maxTicksLimit: 20
                }
            }],
            animation: {
                duration: 0
            }
        }
    });
}

