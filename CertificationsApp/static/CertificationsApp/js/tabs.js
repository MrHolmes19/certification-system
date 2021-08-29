path = window.location.pathname
args = window.location.search

var operations_tab = document.getElementById('v-pills-operation-tab')
var clients_tab = document.getElementById('v-pills-client-tab')
var vehicles_tab = document.getElementById('v-pills-vehicle-tab')

var penddoc_tab = document.getElementById('v-pills-penddoc-tab')
var payconf_tab = document.getElementById('v-pills-payconf-tab')
var pendverif_tab = document.getElementById('v-pills-pendverif-tab')
var pendcert_tab = document.getElementById('v-pills-pendcert-tab')

if(path == '/administrador/'){

    if(args == '?stage=Documentacion%20enviada'){
        penddoc_tab.classList.add('active')
    }
    if(args == '?stage=Pago%20a%20revisar'){
        payconf_tab.classList.add('active')
    }
    if(args == '?stage=Verificacion%20pendiente'){
        pendverif_tab.classList.add('active')
    }
    if(args == '?stage=Esperando%20certificado'){
        pendcert_tab.classList.add('active')
    }

    operations_tab.classList.add('active')
}
if(path == '/administrador/Clientes'){
    clients_tab.classList.add('active')
}
if(path == '/administrador/Vehiculos'){
    vehicles_tab.classList.add('active')
}