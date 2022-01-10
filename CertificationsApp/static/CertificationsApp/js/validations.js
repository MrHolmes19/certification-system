
inputs = document.querySelectorAll('input')

cuitInput = document.querySelector('#cuitInput')
id_numberInput = document.querySelector('#id_id_number')
domainInput = document.querySelector('#id_domain')
phoneInput = document.querySelector('#id_phone')

if(!window.location.pathname.includes("formulario")){
  cuitInput.pattern = '^([^\\d]*\\d[^\\d]*){10,11}$'  // Permite todo, pero limita numeros
  cuitInput.title = "El Cuit debe tener 10 u 11 digitos."

  id_numberInput.pattern = '^([^\\d]*\\d[^\\d]*){7,8}$'  // Permite todo, pero limita numeros
  id_numberInput.title = "El número de documento debe tener entre 7 y 8 digitos."

  domainInput.pattern = '^(?=.*?\\d)(?=.*?[A-Za-z]).{6,9}$' // Debe ser alfanumerico y en total ocupar entre 6 y 8 caracteres
  domainInput.title = "La patente debe ser alfanumérica y poseer entre 6 y 8 caracteres"
}

if(window.location.pathname.includes("formulario")){
  phoneInput.pattern = '^([^\\d]*\\d[^\\d]*){8,15}$'   // Todos los caracteres con minimo 8 numeros
  phoneInput.title = "Ingrese un número de teléfono válido. Puede separar en guiones."
}


