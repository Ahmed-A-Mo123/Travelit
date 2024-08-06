const gridItem1 = document.getElementById('grid-item-1')
const expandButton = document.getElementById('expand-button')
const background = document.getElementById('background')


// Make this an infinate loop and allow the user to exapnd and minimise the grid as much as they want.

function displayResults() {
    // create an element(div) which pops up when expand button is clicked.
    let popUpContainer = document.getElementById('popup-conatiner')
    popUpContainer.setAttribute('class', 'pop-up');
    popUpContainer.setAttribute('id', 'pop-up');
    popUpContainer.innerHTML += `<h1>Results</h1> <button class="btn btn-outline-danger close-button" id="closeButton" ><span class="material-symbols-outlined">
close
</span></button>`;
    
    console.log('This is me the display function');
    let closeButton =document.getElementById('closeButton')
    closeButton.onclick = function(){
        popUpContainer.style.display = 'none';
        console.log('close resilts initated')
    }
};




function main() {
    expandButton.addEventListener('click', function() {
        console.log('ive been clicked');
        displayResults();
    })
    const closeButton = document.getElementById('closeButton');
    
    

};

main();

