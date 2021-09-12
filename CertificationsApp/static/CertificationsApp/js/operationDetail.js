

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
}



