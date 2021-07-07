function getWeather(event) {
    event.preventDefault();
    fetch('/getWeather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'city': document.getElementById('city').value})
    })
    .then(res => {
        // if(res.status == 'ok') console.log('yes');
        console.log(res.status);
        return res.json()
    })
    .then(data => {
        //console.log(data);
        document.getElementById('output').innerHTML = "";
        $('#output').show();
        $('#output').append(`<div class="Location">`+data['region']+`<br><hr></div>`
        +`<div class="parent">`+`<div class="temp">`+data['temperature']+`</div>`+`<div class="condition">`
        +data['time_and_condition'][1]+`</div></div>`+`<div class="time">`+data['time_and_condition'][0]+`</div>`);
    })
    .catch(err => {
        console.log(err);
    })

    // $('#element').css('background', 'url()');

}