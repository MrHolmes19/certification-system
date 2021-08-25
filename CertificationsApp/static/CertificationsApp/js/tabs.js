path = window.location.pathname

var operations_tab = document.getElementById('v-pills-operation-tab')
var clients_tab = document.getElementById('v-pills-client-tab')
var vehicles_tab = document.getElementById('v-pills-vehicle-tab')

if(path == '/administrador/'){
    operations_tab.classList.add('active')
}
if(path == '/administrador/Clientes'){
    clients_tab.classList.add('active')
}
if(path == '/administrador/Vehiculos'){
    vehicles_tab.classList.add('active')
}