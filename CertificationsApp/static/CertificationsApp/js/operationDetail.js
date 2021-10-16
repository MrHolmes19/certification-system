
// giving id to inputs

var myinputs = document.querySelectorAll(".carta input");

i = 1;

myinputs.forEach(input => {
    input.setAttribute('id','input_' + i);
    i++;
    
});

//selecting the hidden input

rejectedImages_input = document.querySelector("#rejectedImages");

// giving id to buttons
var buttons = document.querySelectorAll(".card a");

i = 1;

buttons.forEach(button => {
    button.setAttribute('id','button_' + i);
    i++;
    
});


// i = 1;
// buttons.forEach(button => {
//     button.setAttribute('onclick','document.getElementById("image_' + i + '").src = "../../static/CertificationsApp/images/volver_a_subir.jpeg"');
//     //button.setAttribute('onchange','document.getElementById("image_' + i + '").style.backgroundColor = "yellow"');
//     i++;
    
// });

btn_aprove = document.getElementById('flexRadioDefault1')
btn_reject = document.getElementById('flexRadioDefault2')

function rejectImage(i){
    i = i-12
    console.log(i)
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

// name, surname, mail, phone, id_number
function messageModal(){   
    modal.toggle()
}

// preview images modal

var preview_Modal = new bootstrap.Modal(document.getElementById('PreviewModal'), {keyboard: false})

function previewModal(i){
    preview_Modal.toggle()
    current_image = document.getElementById('image_' + (i-12)).src
    preview_image = document.querySelector(".previewimg");
    preview_image.setAttribute('src', current_image)
}


// setting preview images when uploading
/*
var imageInputs = document.querySelectorAll(".card input");

i = 1;
imageInputs.forEach(input => {
    input.setAttribute('onchange','document.getElementById("image_' + i + '").src = window.URL.createObjectURL(this.files[0])');
    i++;  
});
*/


//blocking the checks if the operation is not aproved

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