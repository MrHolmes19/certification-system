/* adding bootstrap tags to forms */

// login form
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

inputs.forEach(e => {
    e.classList.add("form-control background-color");
});

inputs.forEach(e => {
    e.classList.add("form-label");
});


cuitInput = document.getElementById("cuitInput");
caption = document.getElementById("caption");
var company;


function companyToggle(){

    cuitInput.classList.toggle("d-none");

    console.log(company);

    if(company){
        caption.innerHTML = "¿Sos empresa? hace click";
        company = false;
    } else {
        caption.innerHTML = "¿Sos titular? hace click";
        company = true;
    }
    
}