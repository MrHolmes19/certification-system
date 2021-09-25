
/*------------- CLIENT - HELP ---------------*/

var help_modal = new bootstrap.Modal(document.getElementById('helpModal'), {
    keyboard: false
  })

function helpModal(){
    help_modal.toggle()
}


/*------------- DASHBOARD - CLIENT INFO ---------------*/

var client_modal = new bootstrap.Modal(document.getElementById('clientModal'), {
    keyboard: false
  })

var Mname = document.getElementById('name')
var Msurname = document.getElementById('surname')
var Mid_number = document.getElementById('id_number')
var Memail = document.getElementById('email')
var Mphone = document.getElementById('phone')

function clientModal(name, surname, mail, phone, id_number){
    
    Mname.innerHTML = name
    Msurname.innerHTML = surname
    Mid_number.innerHTML = id_number
    Memail.innerHTML = mail
    Mphone.innerHTML = phone
    
    client_modal.toggle()
}

/*------------- DASHBOARD - PAYMENT CHECKING ---------------*/

var div_modal = document.getElementById('MessageModal')
var modal = new bootstrap.Modal(div_modal, {
    keyboard: false
  })

var Mname = document.getElementById('name')
var Msurname = document.getElementById('surname')
var Mid_number = document.getElementById('id_number')
var Memail = document.getElementById('email')
var Mphone = document.getElementById('phone')

// name, surname, mail, phone, id_number
// PARA QUE CARAJO QUERES TODAS ESTAS VARIABLES? 

function messageModal(){
    modal.toggle()
}


/*------------- DASHBOARD - FEE UPDATING ---------------*/


var fee_modal = new bootstrap.Modal(document.getElementById('feeModal'), {
    keyboard: false
})

function feeModal(){
    console.log(new bootstrap.Modal(document.getElementById('feeModal')));
    fee_modal.toggle()
}