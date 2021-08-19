var modal = new bootstrap.Modal(document.getElementById('clientModal'), {
    keyboard: false
  })

var Mname = document.getElementById('name')
var Msurname = document.getElementById('surname')
var Mid_number = document.getElementById('id_number')
var Memail = document.getElementById('email')
var Mphone = document.getElementById('phone')

// name, surname, mail, phone, id_number
function clientModal(name, surname, mail, phone, id_number){
    
    Mname.innerHTML = name
    Msurname.innerHTML = surname
    Mid_number.innerHTML = id_number
    Memail.innerHTML = mail
    Mphone.innerHTML = phone
    
    modal.toggle()

}

