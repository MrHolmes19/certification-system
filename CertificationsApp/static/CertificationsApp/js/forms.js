
// login form - adding bootstrap style to form

var inputs = document.querySelectorAll("input")

inputs.forEach(e => {
    e.classList.add("form-control");
});

// login form - toggle to company user

let labels = document.querySelectorAll("label")
idNumberLabel = labels[1];
domainLabel = labels[2];
cuitDiv = document.getElementById("inputDiv");
cuitInput = document.getElementById("cuitInput");
company_caption = document.getElementById("caption");
let company;

function companyToggle(){

    cuitDiv.classList.toggle("d-none");
    if(company){
        company_caption.innerHTML = "¿Sos empresa? hace click ";
        idNumberLabel.innerHTML = "DNI"
        domainLabel.innerHTML = "Patente"
        cuitInput.value = ""
        company = false;
    } else {
        company_caption.innerHTML = "¿Sos titular? hace click ";
        idNumberLabel.innerHTML = "DNI del titular"
        domainLabel.innerHTML = "Patente del vehiculo del titular"
        company = true;
    }
}

// login form - toggle to chassis input

chassisDiv = document.getElementById("chassisDiv");
chassisInput = document.getElementById("chassisInput");
chassis_caption = document.getElementById("chassisCaption");
chassisAnchor = document.getElementById("chassisAnchor")
let chassis;

function chassisToggle(){

    chassisDiv.classList.toggle("d-none");
    if(chassis){
        chassis_caption.innerHTML = "¿El vehículo aun no tiene patente? ";
        chassisAnchor.innerHTML = "Entrar con N° de Chasis";
        domainInput.value = "";
        domainLabel.parentElement.hidden = false;
        chassis = false;
    } else {
        chassis_caption.innerHTML = "¿Preferis ingresar con la patente? ";
        chassisAnchor.innerHTML = "Entrar con Patente";
        chassisInput.value = "";
        domainLabel.parentElement.hidden = true;
        chassis = true;
    }
}

// doc form - disabled chassis input when client loged in with that

chassis_doc_input = document.getElementById("id_chassis_number")
if(chassis_doc_input.value != ""){
    chassis_doc_input.readOnly = true
}

// doc form - adding bootstrap style to form

if(window.location.pathname.includes("formulario")){
    let inputs = document.querySelectorAll("input")
    let labels = document.querySelectorAll("label")
    
    inputs.forEach(e => {
        e.classList.add("form-control");
        e.classList.add("background-color");
    });
    
    labels.forEach(e => {
        e.classList.add("form-label");
    });    
}

// doc form - features for company user

const urlParams = new URLSearchParams(window.location.search);
companyParam = urlParams.get('empresa')

if(window.location.pathname.includes("formulario") && companyParam!=""){
    // setting new descriptions
    let labels = document.querySelectorAll("label")
    idNumberLabel = labels[0];
    nameLabel = labels[1];
    surnameLabel = labels[2];
    emailLabel = labels[3];
    phoneLabel = labels[4];
    domainLabel = labels[5];
    idNumberLabel.innerHTML = "DNI del titular" 
    nameLabel.innerHTML = "Nombre del titular"  
    surnameLabel.innerHTML = "Apellido del titular" 
    domainLabel.innerHTML = "Patente del vehiculo del titular"
    
    // setting mail and phone values from company database

    emailInput = document.getElementById("id_mail");
    emailInput.value = document.querySelector("input[name='companyMail']").value
    emailInput.setAttribute("readonly", true)

    phoneInput = document.getElementById("id_phone");
    phoneInput.value = document.querySelector("input[name='companyPhone']").value
    phoneInput.setAttribute("readonly", true)
}

// spinner logic
submit_btn = document.getElementById("form_doc")
submit_btn.addEventListener('submit', loaderStart)
loader = document.getElementById("loader")
inputs.forEach(element => {
    element.addEventListener('invalid', loaderStop)
});

//submit_btn.addEventListener('invalid', logValue)

function loaderStop(e) {
  loader.classList.add("d-none")
}

function loaderStart(e) {
    thanks()
    loader.classList.remove("d-none")
    console.log(e)
  }