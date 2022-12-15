# LOGIN AND REDIRECT

## Access Logic

The application begins with the Login interface, where the client user must log in with her credentials to advance in the process. Due to the multiple alternatives to enter, the different states of each operation and the existing restrictions, a validation and redirection logic was built, which obeys the following diagram

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/diag-logica-de-login-dark.png?raw=true" width="1000">

## Visualization and interaction

We decided to have a single login page and give the user the decision to change the entry inputs according to their condition (owner or representative company) or available information (Patent or vehicle chassis number).

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-cambio-de-inputs.png?raw=true" width="800">

## Validations in the browser

On the browser side, we've put in pattern validations, based on regular expressions, to make sure that the client inputs consistent information. For example, restricting the number of numbers or letters based on the input

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-validacion.png?raw=true" width="800">

We decided to allow entering special characters (eg CUIT with hyphens or separated by thousands with dots) to facilitate the user experience.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-no alfanumericos.png?raw=true" width="800">


## Validations on the server

On the server side, we capture disallowed logins by delivering a message to the user:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-error-op-en-curso.png?raw=true" height="400">  <img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.cliente-login-error-cuit.png?raw=true" height="400">

On the other hand, we have polished the incoming information to eliminate non-alphanumeric characters and normalize the type of data stored and thus avoid errors in future search comparisons.


[--- Next --->>>](doc_form.md#LOAD-DOCUMENTATION)
