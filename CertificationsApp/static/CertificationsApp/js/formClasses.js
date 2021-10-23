
// login form - adding bootstrap style to form

var inputs = document.querySelectorAll("input")

inputs.forEach(e => {
    e.classList.add("form-control");
});

/*   LE DA UN POCO DE PADDING, PERO CREO QUE SE PUEDE QUITAR
labels.forEach(e => {
    e.classList.add("form-label"); 
});
*/

// login form - toggle to company user

let labels = document.querySelectorAll("label")
idNumberLabel = labels[1];
domainLabel = labels[2];
cuitGroupInput = document.getElementById("cuitInput");
cuitInput = document.getElementById("cuit");
caption = document.getElementById("caption");
let company;

function companyToggle(){

    cuitGroupInput.classList.toggle("d-none");
    if(company){
        caption.innerHTML = "¿Sos empresa? hace click";
        idNumberLabel.innerHTML = "DNI"
        domainLabel.innerHTML = "Patente"
        cuitInput.value = ""
        company = false;
    } else {
        caption.innerHTML = "¿Sos titular? hace click";
        idNumberLabel.innerHTML = "DNI del titular"
        domainLabel.innerHTML = "Patente del vehiculo del titular"
        company = true;
    }
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
    // Primer intento
    //emailInput.setAttribute("hidden", true)
    //emailLabel.setAttribute("hidden", true)
    // Segundo intento
    //emailInput.style.setProperty("display","none")
    //emailLabel.style.setProperty("display","none")
    // Tercer intento
    //emailInput.style.setProperty("visibility","hidden")
    //emailInput.style.setProperty("position","absolute")
    //emailLabel.style.setProperty("visibility","hidden")
    //emailLabel.style.setProperty("position","absolute")

    phoneInput = document.getElementById("id_phone");
    phoneInput.value = document.querySelector("input[name='companyPhone']").value
    phoneInput.setAttribute("readonly", true)
}

