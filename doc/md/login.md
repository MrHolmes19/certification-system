# INGRESO Y REDIRECCIONAMIENTO

## Lógica de acceso

El aplicativo comienza con la interfaz de Login, donde el usuario cliente deberá loguearse con sus credenciales para avanzar en el proceso. Debido a las múltiples alternativas para ingresar, los distintos estados de cada operación y las restricciones existentes, se construyó una lógica de validación y redirección, que obedece al siguiente diagrama

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/diag-logica-de-login.png?raw=true" width="800">

## Visualización e interacción 

Decidimos tener una sola página de login, y darle al usuario la decisión de cambiar los inputs de ingreso de acuerdo a su condición o información disponible

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-cambio-de-inputs.png?raw=true" width="800">

## Validaciones en el navegador

Del lado del navegador, hemos puesto validaciones con patrones basados en expresiones regulares, para asegurarnos de que el cliente ingrese información coherente. Por ejemplo, restringiendo la cantidad de números o letras según el input

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-validacion.png?raw=true" width="800">

Decidimos permitir ingresar caracteres especiales (Ej. CUIT con guiones o separado por miles con puntos) para facilitar la experiencia de usuario.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-no alfanumericos.png?raw=true" width="800">


## Validaciones en el servidor

Del lado del servidor, se captura los ingresos no permitidos entregando un mensaje al usuario:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-error-op-en-curso.png?raw=true" width="400">  <img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-error-cuit.png?raw=true" width="400">

Por otro lado, hemos pulido la información entrante para eliminar caracteres no alfanuméricos y normalizar el tipo de dato almacenado, y así evitar errores en comparaciones de búsqueda a futuro.
