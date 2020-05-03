var x = 0;
var temperature = 0;
var humidity = 0;
var soil_moisture = 0;

var ctx = $("#temperature_chart");
console.log("test");
var temperature_chart = new Chart(ctx, {

    type: 'line',
    data: {
        labels: [],
        datasets : [
            {
                label: 'temperature',
                data: [],
                borderColor: [
                    '#060666',
                ],
                borderWidth: 3,
                fill: false
            },
            

            {
                label: 'Humidity',
                data: [],
                borderColor: [
                    '#d6c73e'
                ],
                fill: false
            }, 

            {
                label: 'Soil Moisture',
                data: [],
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


var updated_data  = $.get('/update');

updated_data.done(function(results){
    temperature = results.results[0];
    humidity = results.results[1];
    soil_moisture = results.results[2];
    x = results.results[3];
    // console.log(temperature);
    // console.log(humidity);
    // console.log(soil_moisture);
    temperature_chart.data.datasets[0].data = temperature;
    temperature_chart.data.datasets[1].data = humidity;
    temperature_chart.data.datasets[2].data = soil_moisture;
    temperature_chart.data.labels = x;

    temperature_chart.update();

    });

setInterval(function(){
    var getData = $.get('/start');
    console.log(x)
    x = parseInt(x[x.length -1]);
    console.log(x)
    x =  (x+30).toString();
    console.log(x)
    getData.done(function(results){
        temperature = results.results[0];
        humidity = results.results[1];
        soil_moisture = results.results[2];
        // console.log(temperature);
        // console.log(humidity);
        // console.log(soil_moisture);
        temperature_chart.data.labels.push(x);
        temperature_chart.data.datasets[0].data.push(temperature);
        temperature_chart.data.datasets[1].data.push(humidity);
        temperature_chart.data.datasets[2].data.push(soil_moisture);
    });
    
    temperature_chart.update();

},180000); //90000


