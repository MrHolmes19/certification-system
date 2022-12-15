# TURN SYSTEM

## Client Side

After making the payment, the client will access an interface to request a shift. You must choose the date from a drop-down list (not later than 4 weeks) and then select from the available times:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/4.cliente-turno-fecha.png?raw=true" width="800">

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/4.cliente-turno-horario.png?raw=true" width="800">

After reserving the shift, the operation will go to the "Pending verification" status and the user will be redirected to an interface with the reservation data:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/4.cliente-turno-concertado.png?raw=true" width="800">


## Admin Side

The administrator has a special section for shifts on the dashboard, where he can view shifts already assigned and not yet occupied and block some schedules in advance.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/4.admin-tabla-turnos.png?raw=true" width="900">

From the detail of operations, it is possible to assign a shift to the customer.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/4.admin-asignacion de turno.png?raw=true" width="800">

It is also possible to reject an already arranged appointment, or reject the vehicle verification if the vehicle is not suitable for approval. In both cases, the operation will return to the "Pending turn" status, redirecting the client to the previous step. If the vehicle verification is approved, the operation will go to the final state that is "Waiting for certificate".

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/4.admin-aprobacion-verif-vehicular.png?raw=true" width="600">


[--- Next --->>>](pdf_inform.md#PDF-REPORT-GENERATION)
