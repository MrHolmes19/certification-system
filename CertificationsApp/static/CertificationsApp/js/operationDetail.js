
// giving id to inputs

var myinputs = document.querySelectorAll(".carta input");

i = 1;

myinputs.forEach(input => {
    input.setAttribute('id','input_' + i);
    i++;
    
});


// giving id to buttons

var buttons = document.querySelectorAll(".card a");

i = 1;

buttons.forEach(button => {
    button.setAttribute('id','button_' + i);
    i++;
    
});

// setting default image for rejected ones

rejectedImages_input = document.querySelector("#rejectedImages");
btn_aprove = document.getElementById('flexRadioDefault1')
btn_reject = document.getElementById('flexRadioDefault2')

function rejectImage(i){
    i = i-12
    document.getElementById("image_" + i).src = "../../static/CertificationsApp/images/volver_a_subir.jpeg"
    previous_value = rejectedImages_input.value
    rejectedImages_input.value += "-image"+i+"_uploaded"
    btn_aprove.setAttribute("disabled", true)
    btn_reject.click()
    blockChecks()
}

var div_modal = document.getElementById('MessageModal')
var modal = new bootstrap.Modal(div_modal, {
    keyboard: false
})

function messageModal(){   
    modal.toggle()
}


// appointmentModal
var appointment_Modal = new bootstrap.Modal(document.getElementById('appointmentModal'), {keyboard: false})

function appointmentModal(){   
    appointment_Modal.toggle()
}



// preview images modal

var preview_Modal = new bootstrap.Modal(document.getElementById('PreviewModal'), {keyboard: false})

function previewModal(i){
    preview_Modal.toggle()
    current_image = document.getElementById('image_' + (i-12)).src
    preview_image = document.querySelector(".previewimg");
    preview_image.setAttribute('src', current_image)
}

// blocking checkbuttons if the operation is not aproved

function blockChecks(){
    let checks = document.querySelectorAll(".jumpChecks input")

    checks.forEach(check => {
        check.checked = false
        check.setAttribute("disabled", true)
    });
    }

function unblockChecks(){
    let checks = document.querySelectorAll(".jumpChecks input")
    
    checks.forEach(check => {
        check.removeAttribute("disabled")
    });
    }

btn_reject.addEventListener("click", blockChecks)
btn_aprove.addEventListener("click", unblockChecks)

// Disable all buttons when operation is inactive and show toggle button when check is click

let stateSwitch = document.getElementById("stateSwitch")
let switchLabel = document.getElementById("switchLabel")
let stateButton = document.getElementById("stateButton")
const onloadState = stateSwitch.checked
let currentState = stateSwitch.checked

stateButton.hidden = true

if(currentState == false){ //inactive
    switchLabel.innerHTML = "Operacion Inactiva"
    allButtons = document.querySelectorAll(".btn")
    allButtons.forEach( button =>{
        button.disabled = true
    });
}else { //active
    allButtons = document.querySelectorAll(".btn")
    allButtons.forEach( button =>{
        button.disabled = false
    });
}

function toggleState(){
    currentState = stateSwitch.checked
    // console.log("current es check: " + currentState)
    // console.log("onload es check: " + onloadState)
    if(currentState!=onloadState){
        stateButton.hidden = false
        stateButton.disabled = false
    }else{
        stateButton.hidden = true
    }
    if(currentState == false){
        switchLabel.innerHTML = "Operacion Inactiva"
        stateSwitch.value = "off"
        // console.log("Entró en false. HTML: ")
        // console.log(stateSwitch)
        // console.log("Entró en false. Valor del input: " + stateSwitch.value)
    }else{
        switchLabel.innerHTML = "Operacion Activa"
        stateSwitch.value = "on"
        // console.log("Entró en true. HTML: ")
        // console.log(stateSwitch)
        // console.log("Entró en true. Valor del input: " + stateSwitch.value)
    }
}

if(!can_change_doc){
    alert("you cant change the doc")

    const client_doc = document.getElementById('client_doc_form')
    const client_inputs = client_doc.querySelectorAll('input')
    const client_buttons = client_doc.querySelectorAll('.btn')

    client_inputs.forEach(inp => {
        inp.disabled = true
    });

    client_buttons.forEach(btn => {
        btn.classList.add('disabled')
    });
}