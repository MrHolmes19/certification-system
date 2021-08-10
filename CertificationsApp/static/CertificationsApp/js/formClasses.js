// login form

var loginform = document.getElementById("loginform");




//Doc form

var inputs = document.querySelectorAll("input");
var labels = document.querySelectorAll("label");

inputs.forEach(e => {
    e.classList.add("form-control background-color");
});

inputs.forEach(e => {
    e.classList.add("form-label");
});

