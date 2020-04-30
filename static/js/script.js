var x = 0;
var temperature = 0;
var humidity = 0;

var ctx = $("#temperature_chart");
var temperature_chart = new Chart(ctx, {

    type: 'line',
    data: {
        labels: [x],
        datasets : [
            {
                label: 'temperature',
                data: [temperature],
                borderColor: [
                    '#060666',
                ],
                borderWidth: 3,
                fill: false
            },
            

            {
                label: 'Humidity',
                data: [humidity],
                borderColor: [
                    '#7fced4'
                ],
                fill: false
            }
        ]
    },
    
    options: {
        responsive: false,

    }

});



setInterval(function(){
    var getData = $.get('/start');
    x = x+1;
    
    getData.done(function(results){
        temperature = results.results[0];
        humidity = results.results[1];
        //console.log(temperature);

        temperature_chart.data.labels.push(x.toString());
        temperature_chart.data.datasets[0].data.push(temperature);
        temperature_chart.data.datasets[1].data.push(humidity);
    });
    
    temperature_chart.update();


},1500);
