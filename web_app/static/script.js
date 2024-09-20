document.getElementById('predict-btn').addEventListener('click', function() {
    const soilMoisture = document.getElementById('soil_moisture').value;
    const temperature = document.getElementById('temperature').value;
    const humidity = document.getElementById('humidity').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            soil_moisture: soilMoisture,
            temperature: temperature,
            humidity: humidity
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction').innerText = data.needs_watering === 1 ? 'Needs Watering' : 'No Watering Needed';
    })
    .catch(error => console.error('Error:', error));
});
