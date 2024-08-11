const gridItem1 = document.getElementById('grid-item-1')
const expandButton1 = document.getElementById('expand-button-1')
const expandButton2 = document.getElementById('expand-button-2')
const expandButton3 = document.getElementById('expand-button-3')
const expandButton4 = document.getElementById('expand-button-4')
const background = document.getElementById('background')



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



// --------------------------------------------------------------------------------------------------------------------------------------------------------------------
function main() {
    // This is the main function which serves an event listerner and calls the relevant function to execute when triggered

    // create a key-pair dictionary/ hash map to send the user input details to the api
    const userData = new FormData();
    userData.append('origin', window.origin ) 
    userData.append('destination',window.destination) 
    userData.append('passengers',window.passengers) 
    userData.append('departure_date', window.departure_date) 
    userData.append('return_date', window.return_date) 
    

    // Send an AJAX POST request to the Django view
    fetch('api_request/', {
        method: 'POST',
        body: userData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest' } // Necessary for Django to recognize AJAX request
    })
        .then(response => response.json())
        .then(data => {}) 
        // test if the api is returning correctly and everything is working in order.
        .catch(error => console.error('Error:', error));




    expandButton1.addEventListener('click', function() {
        console.log('ive been clicked');
        console.log(window.passengers);
        console.log(userData)
        displayResults();
    })
    expandButton2.addEventListener('click', function() {
        console.log('ive been clicked');
        displayResults();
    })
    expandButton3.addEventListener('click', function() {
        console.log('ive been clicked');
        displayResults();
    })
    expandButton4.addEventListener('click', function() {
        console.log('ive been clicked');
        displayResults();
    })
    
    

};


// run the main function
main();

