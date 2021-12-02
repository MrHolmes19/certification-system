path = window.location.pathname
args = window.location.search
activeClass = ['bg-primary', 'text-white']

var operations_tab = document.getElementById('operation-tab')
var clients_tab = document.getElementById('client-tab')
var vehicles_tab = document.getElementById('vehicle-tab')
var company_tab = document.getElementById('company-tab')

var penddoc_tab = document.getElementById('penddoc-tab')
var payconf_tab = document.getElementById('payconf-tab')
var pendverif_tab = document.getElementById('pendverif-tab')
var pendcert_tab = document.getElementById('pendcert-tab')

var search_tab = document.getElementById('search-tab')
var fee_tab = document.getElementById('fee-tab')
var appointments_tab = document.getElementById('appointments-tab')
var stats_tab = document.getElementById('stats-tab')

if(path == '/administrador/Busqueda'){
    search_tab.classList.add(activeClass[0],activeClass[1])
}
if(path == '/administrador/tarifas'){
    fee_tab.classList.add(activeClass[0],activeClass[1])
}
if(path == '/administrador/turnos'){
    appointments_tab.classList.add(activeClass[0],activeClass[1])
}
if(path == '/administrador/Estadisticas'){
    stats_tab.classList.add(activeClass[0],activeClass[1])
}

if(path == '/administrador/'){

    if(args == '?stage=Documentacion%20enviada'){
        penddoc_tab.classList.add(activeClass[0],activeClass[1])
    }
    if(args == '?stage=Pago%20a%20revisar'){
        payconf_tab.classList.add(activeClass[0],activeClass[1])
    }
    if(args == '?stage=Verificacion%20pendiente'){
        pendverif_tab.classList.add(activeClass[0],activeClass[1])
    }
    if(args == '?stage=Esperando%20certificado'){
        pendcert_tab.classList.add(activeClass[0],activeClass[1])
    }

    operations_tab.classList.add(activeClass[0],activeClass[1])
}

if(path == '/administrador/Clientes'){
    clients_tab.classList.add(activeClass[0],activeClass[1])
}
if(path == '/administrador/Vehiculos'){
    vehicles_tab.classList.add(activeClass[0],activeClass[1])
}
if(path == '/administrador/Empresas'){
    company_tab.classList.add(activeClass[0],activeClass[1])
}
if(path == '/administrador/turnos'){
    appointments_tab.classList.add(activeClass[0],activeClass[1])
}