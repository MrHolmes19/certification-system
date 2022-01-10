# CARGA DE DOCUMENTACION

## Lado Cliente

Luego del ingreso, el usuario deberá completar algunos campos con datos de contacto, información del vehículo (Que luego se utilizará para crear el informe en pdf). Estos inputs poseen también validaciones en el front y en el back.

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.cliente-formulario.png?raw=true" width="800">

Al seleccionar las listas desplegables de los últimos inputs, se renderizan unas “cards” con las fotos necesarias en función del tipo de cambio que el cliente desee realizar en su vehículo.

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.cliente-selects.png?raw=true" width="800">

Para cargar las imágenes, basta con hacer click sobre la misma y habilitará al usuario a seleccionar un archivo de su dispositivo (Válido en versión escritorio y mobile)

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.cliente-formulario-carga-imagen.png?raw=true" width="800">

Luego de completar el formulario y presionar el botón de enviar, si todos los campos fueron completados y pasan las validaciones, se habilitará el logo dinámico de carga y luego redirigirá a una interfaz de envío exitoso

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.cliente-formulario-envio-formulario.png?raw=true" width="800">

El usuario podrá acceder a una ayuda ventana de ayuda

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.cliente-formulario-boton-ayuda.png?raw=true" width="800">

Si el administrador rechaza la documentación por posibles inconsistencias, el usuario ingresará nuevamente al formulario, pudiendo solo modificar aquello que fue rechazado, por ejemplo, ciertas fotos:

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.cliente-formulario-rechazado.png?raw=true" width="800">


## Lado Administrador

Desde el tablero de comando, se puede filtrar por aquellas operaciones que están pendientes de revisión

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.admin-operaciones-pendientes-de-revision.png?raw=true" width="800">

Cliqueando en la lupa, se accede al “Detalle” de la operación. El primer encabezado del acordeón contiene la información de la documentación enviada por el cliente, y es desde ahí donde se puede aceptar o rechazar la documentación.

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.admin-detalle documentacion cargada.png?raw=true" width="800">

El administrador puede abrir cada foto para verla en zoom (o bien descargarla) haciendo click en el botón “ver imagen” de la tarjeta:

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.admin-doc-vista-previa-imagen.png?raw=true" width="800">

En caso de que alguna foto no corresponda, o bien su nitidez no sea la adecuada, puede presionar el botón de “rechazar foto”, esto asignará una foto por defecto, que luego es la que verá el cliente al volver a ingresar al link.

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.admin-rechazo-foto-formulario.png?raw=true" width="800">

En caso de que el cliente sea una empresa que representa un titular, el administrador podrá seleccionar un “check” para saltarse el pago y otro para saltarse el turno para verificación vehicular.

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/2.admin-doc-aprobacion-con-salto.png?raw=true" width="800">

