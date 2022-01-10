# SISTEMA DE TURNOS

## Lado Cliente

Luego de realizar el pago, el cliente accederá a una interfaz para solicitar un turno. Deberá elegir de una lista desplegable la fecha (No posterior a 2 semanas) y luego seleccionar entre los horarios disponibles:

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/4.cliente-turno-fecha.png?raw=true" width="800">

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/4.cliente-turno-horario.png?raw=true" width="800">

Luego de reservar el turno la operación pasará a “Verificación pendiente” y el usuario será redireccionado a una interfaz con los datos de su reserva:

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/4.cliente-turno-concertado.png?raw=true" width="800">


## Lado Administrador

El administrador posee en el tablero de comando, una sección especial para los turnos, donde podrá visualizar los turnos ya asignados y aun no ocupados y bloquear de antemano algunos horarios.

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/4.admin-tabla-turnos.png?raw=true" width="800">

Desde el detalle de operaciones, es posible asignar un turno al cliente.

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/4.admin-asignacion de turno.png?raw=true" width="800">

También es posible rechazar una cita ya concertada, o rechazar la verificación vehicular si el vehículo no esta apto para su aprobación. En ambos casos la operación volverá al estado de “Turno pendiente” redireccionando al cliente al paso anterior. Si se aprueba la verificación vehicular la operación pasará al estado final que es “Esperando certificado”.

<img src="https://github.com/MrHolmes19/certification-system/doc/screenshots/4.admin-aprobacion-verif-vehicular.png?raw=true" width="800">
