
inputs = document.querySelectorAll('input')

cuitInput = document.querySelector('#cuitInput')
id_numberInput = document.querySelector('#id_id_number')
domainInput = document.querySelector('#id_domain')
phoneInput = document.querySelector('#id_phone')

if(!window.location.pathname.includes("formulario")){
  cuitInput.pattern = '^([^\\d]*\\d[^\\d]*){10,11}$'  // Allows everything, just limiting numbers
  cuitInput.title = "El Cuit debe tener 10 u 11 digitos."

  //id_numberInput.pattern = '^([^\\d]*\\d[^\\d]*){7,8}$'  // Allows everything, just limiting numbers
  // id_numberInput.title = "El número de documento debe tener entre 7 y 8 digitos."

  id_numberInput.pattern = '^(([^\\d]*\\d[^\\d]*){7,8}|([^\\d]*\\d[^\\d]*){10,11})$'  // Allows everything, just limiting numbers
  id_numberInput.title = "inserte DNI entre 7 y 8 digitos o CUIL entre 10 y 11."

  domainInput.pattern = '^(?=.*?\\d)(?=.*?[A-Za-z]).{6,9}$' // Must be alphanumeric and be between 6 and 8 characters
  domainInput.title = "La patente debe ser alfanumérica y poseer entre 6 y 8 caracteres"
}

if(window.location.pathname.includes("formulario")){
  phoneInput.pattern = '^([^\\d]*\\d[^\\d]*){8,15}$'   // All characteres with 8 numbers at least
  phoneInput.title = "Ingrese un número de teléfono válido. Puede separar en guiones."
}


