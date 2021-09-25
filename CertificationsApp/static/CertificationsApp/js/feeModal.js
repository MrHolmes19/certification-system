var fee_modal = new bootstrap.Modal(document.getElementById('feeModal'), {
    keyboard: false
})

currentFee = document.getElementById('currentFee')
type_label = document.getElementById('feeModalLabel')
selected_type = document.getElementById('selected_type')


function feeModal(available_type, fee){
    type_label.innerHTML = "Tarifa de " + available_type
    currentFee.value = fee
    selected_type.value = available_type
    fee_modal.toggle()
}