var company_modal = new bootstrap.Modal(document.getElementById('companyModal'), {
    keyboard: false
})

var newCompany_modal = new bootstrap.Modal(document.getElementById('createCompanyModal'), {
    keyboard: false
})


nameInput = document.getElementById('companyName')
cuitInput = document.getElementById('companyCuit')
mailInput = document.getElementById('companyMail')
phoneInput = document.getElementById('companyPhone')
idInput = document.getElementById('company_id')

radioEnabled = document.getElementById('enabled')
radioDisabled = document.getElementById('disabled')

function updateModal(cuit, name, mail, phone, enabled, id){
    nameInput.value = name
    cuitInput.value = cuit
    mailInput.value = mail
    phoneInput.value = phone
    idInput.value = id
    if(enabled == "True"){
        radioEnabled.checked = true
    } else {
        radioDisabled.checked = true
    }

    company_modal.toggle()
}


