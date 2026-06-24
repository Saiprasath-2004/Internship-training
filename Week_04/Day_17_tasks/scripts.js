console.log("JavaScript Connected");

let learning = [];

let themeButton = document.querySelector("#theme-toggle");

themeButton.addEventListener("click",function(){
    console.log("Button Clicked")
    document.body.classList.toggle("dark-theme");

    if(document.body.classList.contains("dark-theme")){
        themeButton.textContent="Light Mode";
    }
    else{
        themeButton.textContent="Dark Mode";
    }
})


let inputBox = document.querySelector("#learning-input");
let addButton = document.querySelector("#add-learning");
let learningList = document.querySelector("#learning-items");


function addLearning(){
    if(inputBox.value === ""){

        alert("Please enter something");

        return;
    }   
    learning.push(inputBox.value);
    let listItem = document.createElement("li");
    listItem.textContent = inputBox.value;
    learningList.appendChild(listItem);
     inputBox.value = "";
    console.log(learning);
}

addButton.addEventListener("click", addLearning);

inputBox.addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        addLearning();
    }

});

let quoteButton = document.querySelector("#get-quote");

let quoteDisplay = document.querySelector("#quote-display");


quoteButton.addEventListener("click", function(){

    fetch("https://dummyjson.com/quotes/random")

        .then(function(response){

            return response.json();

        })

        .then(function(data){
            console.log(data);

            quoteDisplay.textContent = 

            data.quote + " — " + data.author;

        });

});