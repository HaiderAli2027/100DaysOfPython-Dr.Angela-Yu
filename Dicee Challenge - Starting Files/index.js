var randomNumb1 = Math.floor(Math.random() * 6) + 1;
var randomImage1 = "dice"+randomNumb1+".png";
var randomImageSource1 = "images/"+randomImage1;

var image1 = document.querySelectorAll("img")[0];

image1.setAttribute("src",randomImageSource1);

var randomNumb2 = Math.floor(Math.random() * 6) + 1;
var randomImageSource2 = "images/dice"+randomNumb2+".png";

document.querySelectorAll("img")[1].setAttribute("src", randomImageSource2);

if(randomNumb1 > randomNumb2){
    document.querySelector("h1").innerHTML = "🚩Player1 is win!"
}
else if(randomNumb1 < randomNumb2){
    document.querySelector("h1").innerHTML = "Player2 is win!🚩"
}
else{
        document.querySelector("h1").innerHTML = "Draw!"
}