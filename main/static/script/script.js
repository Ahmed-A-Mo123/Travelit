const gridItem1 = document.getElementById('grid-item-1')
const gridItem2 = document.getElementById('grid-item-2')
const gridItem3 = document.getElementById('grid-item-3')
const gridItem4 = document.getElementById('grid-item-4')
const expandButton1 = document.getElementById('expand-button-1')
const expandButton2 = document.getElementById('expand-button-2')
const expandButton3 = document.getElementById('expand-button-3')
const expandButton4 = document.getElementById('expand-button-4')
const background = document.getElementById('background')
let loader1 = document.getElementById('loader1')
let loader2 = document.getElementById('loader2')
let complete1 = document.getElementById('complete1')
let complete2 = document.getElementById('complete2')
let complete3 = document.getElementById('complete3')
let complete4 = document.getElementById('complete4')


function getDayName(dateStr) // This function helps convert a date string into a day to use in the weather section
{
    var date = new Date(dateStr);
    return date.toLocaleDateString('en-GB', { weekday: 'short' });        
}








// -------------------------------------------------------------------------------------------------------------------------------------------------------------------
function displayResults() {
    // This function allows the user to expand the view of their results (a pop-up). It also checks if the pop-up element is being displayed before creating a fresh pop-up
    // add parameteres so i can pass through arguments which are displayed to the user.

    let existingPopup = document.getElementById('pop-up'); 
    if (existingPopup) {
        existingPopup.remove();
    }

    let popUpContainer = document.createElement('div');
    popUpContainer.setAttribute('class', 'pop-up');
    popUpContainer.setAttribute('id', 'pop-up');
    popUpContainer.innerHTML = `<h1>Results</h1> <button class="btn btn-outline-danger close-button" id="closeButton" ><span class="material-symbols-outlined">close
    </span></button> 
    <div class="result-item">LON TO KUL</div>
    <div class="result-item">LON TO KUL</div>
    <div class="result-item">LON TO KUL</div>
    <div class="result-item">LON TO KUL</div>
    <div class="result-item">LON TO KUL</div>
    `;

    document.body.appendChild(popUpContainer);
    
    console.log('This is me the display function');
    let closeButton = document.getElementById('closeButton')
    closeButton.onclick = function(){
        popUpContainer.style.display = 'none';
        console.log('close results initated')
    }
};

function displayWeather(data) {

    const daylist = [data['forecast']['forecastday'][0]['date'], // forcast date 1
                     data['forecast']['forecastday'][1]['date'], // forcast date 2
                     data['forecast']['forecastday'][2]['date']  // forcast date 3
                    ]

    var day1 = getDayName(daylist[0]) // converts full date in the day
    var day2 = getDayName(daylist[1])
    var day3 = getDayName(daylist[2])

    var day1Icon = data['forecast']['forecastday'][0]['day']['condition']['icon']
    var day2Icon = data['forecast']['forecastday'][1]['day']['condition']['icon']
    var day3Icon = data['forecast']['forecastday'][2]['day']['condition']['icon']
    
    var maxTemp1 = data['forecast']['forecastday'][0]['day']['maxtemp_c']
    var maxTemp2 = data['forecast']['forecastday'][1]['day']['maxtemp_c']
    var maxTemp3 = data['forecast']['forecastday'][2]['day']['maxtemp_c']

    var conditionText1 = data['forecast']['forecastday'][0]['day']['condition']['text']
    var conditionText2 = data['forecast']['forecastday'][1]['day']['condition']['text']
    var conditionText3 = data['forecast']['forecastday'][2]['day']['condition']['text']

    console.log(data['forecast']['forecastday'][0]['date'])
    const weatherGrid = document.createElement('div')
    weatherGrid.className = 'weather-container'
    
    // const weatherRow = document.createElement('div')
    // weatherRow.className = ''

    const weatherItem1 = document.createElement('div')
    weatherItem1.className = 'weather-col'
    weatherItem1.innerHTML = `<p>${day1}</p><img src="https://${day1Icon}" alt="weather icon" class="weather-icon"><p>${maxTemp1}</p><p>${conditionText1}</p>`

    const weatherItem2 = document.createElement('div')
    weatherItem2.className = 'weather-col'
    weatherItem2.innerHTML = `<p>${day2}</p><img src="https://${day2Icon}" alt="weather icon" class="weather-icon"><p>${maxTemp2}<</p><p>${conditionText2}</p>`

    const weatherItem3 = document.createElement('div')
    weatherItem3.className = 'weather-col'
    weatherItem3.innerHTML = `<p>${day3}</p><img src="https://${day3Icon}" alt="weather icon" class="weather-icon"><p>${maxTemp3}<</p><p>${conditionText3}</p>`

    weatherGrid.append(weatherItem1, weatherItem2, weatherItem3)

    gridItem2.appendChild(weatherGrid)

}

function displayChatGPT() {
    const chatGptOptions = document.createElement('div')
    chatGptOptions.className = 'chatgpt-container'
    
    chatGptOptions.innerHTML = 
                `<button type="button" class="btn btn-outline-primary chatgpt-col">Destinations Info</button>
                <button type="button" class="btn btn-outline-primary chatgpt-col">Things To Do</button>
                <button type="button" class="btn btn-outline-primary chatgpt-col">Best Time To Go</button>
                <button type="button" class="btn btn-outline-primary chatgpt-col">Other Reconmended Places </button>
                `
    gridItem4.appendChild(chatGptOptions)
}


// --------------------------------------------------------------------------------------------------------------------------------------------------------------------
function main() {
    // This is the main function which serves an event listerner and calls the relevant function to execute when triggered

    // create a key-pair dictionary/ hash map to send the user input details to the api
    window.onload = () => {
        const userData = new FormData();
        userData.append('origin', window.origin );
        userData.append('destination',window.destination); 
        userData.append('passengers',window.passengers);
        userData.append('departure_date', window.departure_date); 
        userData.append('return_date', window.return_date);


        fetch('weather_request/', {
            method: 'POST',
            body: userData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest' // Necessary for Django to recognize AJAX request
            }
        })
        .then(response => response.json())
        .then(weatherData => {
            if (weatherData.error) {
                console.log('Error with the weather data');
            } else {
                loader2.style.display = 'none';
                complete2.style.display = 'none'; // Instead of a green tick display the results of the weather inside the div
                console.log('Data received from server:', weatherData);
                console.log('WEATHER DATA FINISHED LOADING');
        
                displayWeather(weatherData);
            }
        })
        .catch(error => console.error('Fetch weather data error:', error));


        // Flight Data Request
        fetch('flights_request/', {
            method: 'POST',
            body: userData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest' // Necessary for Django to recognize AJAX request
            }
        })
        .then(response => response.json())
        .then(flightData => {
            if (flightData.error) {
                console.log('Error with the flight data');
            } else {
                loader1.style.display = 'none';
                complete1.style.display = 'block';
                console.log('Data received from server:', flightData);
                console.log('FLIGHT DATA FINISHED LOADING');

                expandButton1.classList.remove('btn-outline-dark');
                expandButton1.classList.add('btn-outline-success');

                expandButton1.addEventListener('click', function() {
                    console.log('ive been clicked');
                    console.log(window.passengers);
                    console.log(userData);
                    displayResults();
                });
            }
        })
        .catch(error => console.error('Fetch flight data error:', error));


        // ChatGpt reuest -- note may need to change how many request we make to the ai and then put in a list/dict to access it all at once here
        fetch('chatGPT_request/', {
            method: 'POST',
            body: userData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest' // Necessary for Django to recognize AJAX request
            }
        })
        .then(response => response.json())
        .then(ChatGPTData => {
            if (ChatGPTData.error) {
                console.log('Error with the weather data');
            } else {
                loader2.style.display = 'none';
                complete2.style.display = 'none'; // Instead of a green tick display the results of the weather inside the div
                console.log('Data received from server:', ChatGPTData);
                console.log('WEATHER DATA FINISHED LOADING');
        
                displayChatGPT() 
            }
        })
        .catch(error => console.error('Fetch weather data error:', error));



        







              //         expandButton1.addEventListener('click', function() {
        //             console.log('ive been clicked');
        //             console.log(window.passengers);
        //             console.log(userData)
        //             displayResults();
        //         })

            expandButton3.addEventListener('click', function() {
                console.log('ive been clicked');
                displayResults();
            })
            expandButton4.addEventListener('click', function() {
                console.log('ive been clicked');
                displayResults();
            })


    }





    
    

};


// run the main function
main();

