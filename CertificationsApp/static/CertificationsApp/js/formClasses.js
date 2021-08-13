// login form
<<<<<<< HEAD

var loginform = document.getElementById("loginform");




//Doc form

var inputs = document.querySelectorAll("input");
var labels = document.querySelectorAll("label");
=======
var inputs = document.querySelectorAll("input")
var labels = document.querySelectorAll("label")

inputs.forEach(e => {
    e.classList.add("form-control");
});

inputs.forEach(e => {
    e.classList.add("form-label");
});


// doc form
var inputs = document.querySelectorAll("input")
var labels = document.querySelectorAll("label")
>>>>>>> 440132a

inputs.forEach(e => {
    e.classList.add("form-control background-color");
});

inputs.forEach(e => {
    e.classList.add("form-label");
});

