
inputs = document.querySelectorAll('input')

cuitInput = document.querySelector('#cuitInput')
id_numberInput = document.querySelector('#id_id_number')
domainInput = document.querySelector('#id_domain')
phoneInput = document.querySelector('#id_phone')

if(!window.location.pathname.includes("formulario")){
  //cuitInput.pattern = "^[\\d]{2,2}[\\.,-]?[\\d]{1,2}[\\.,-]?[\\d]{3,3}[\\.,-]?[\\d]{3,3}[\\.,-]?[\\d]{1,1}$"
  //cuitInput.title = "El Cuit debe tener 10 u 11 digitos. Se permiten puntos, comas y guiones"

  //cuitInput.pattern = "^[0-9-+()]*$"
  //cuitInput.pattern = "^[\\d.]{10,11}$"
  //cuitInput.pattern = "^[0-9-+()]{10,11}$"
  cuitInput.pattern = '^([^\\d]*\\d[^\\d]*){10,11}$'  // Permite todo, pero limita numeros
  cuitInput.title = "El Cuit debe tener 10 u 11 digitos."


  // id_numberInput.pattern = "^[\\d]{1,2}[\\.,-]?[\\d]{3,3}[\\.,-]?[\\d]{3,3}[\\.,-]?[\\d]{1,1}$"
  // id_numberInput.title = "El número de documento debe tener entre 7 y 8 digitos. Se permiten puntos, comas y guiones"
  id_numberInput.pattern = '^([^\\d]*\\d[^\\d]*){7,8}$'  // Permite todo, pero limita numeros
  id_numberInput.title = "El número de documento debe tener entre 7 y 8 digitos."

  //domainInput.pattern = "^[\\d]{2,2}[\\.,-]?[\\d]{1,2}[\\.,-]?[\\d]{3,3}[\\.,-]?[\\d]{3,3}[\\.,-]?[\\d]{1,1}$"
  //domainInput.title = "La patente debe ser alfanumérica y poseer minimo 6 caracteres"
  //domainInput.pattern = '^([^\\w]*\\w[^\\w]*){6,8}$'  // Permite todo, pero limita alfanumericos alt: ^[A-Za-z0-9]*$
  domainInput.pattern = '^(?=.*?\\d)(?=.*?[A-Za-z]).{6,9}$' // Debe ser alfanumerico y en total ocupar entre 6 y 8 caracteres
  domainInput.title = "La patente debe ser alfanumérica y poseer entre 6 y 8 caracteres"
}

if(window.location.pathname.includes("formulario")){
  phoneInput.pattern = '^([^\\d]*\\d[^\\d]*){8,15}$'   // Todos los caracteres con minimo 8 numeros
  phoneInput.title = "Ingrese un número de teléfono válido. Puede separar en guiones."
}


