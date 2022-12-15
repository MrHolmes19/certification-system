# DOCUMENTATION LOAD

## Client Side

After entering, the user must complete some fields with contact information, vehicle information (which will later be used to create the report in pdf). These inputs also have front and back validations.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.cliente-formulario.png?raw=true" width="800">

By selecting the drop-down lists of the last inputs, "cards" are rendered with the necessary photos depending on the type of change that the customer wishes to make to their vehicle.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.cliente-formulario-selects.png?raw=true" width="800">

To load the images, just click on it and it will enable the user to select a file from their device (Valid in desktop and mobile version)

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.cliente-formulario-carga-imagen.png?raw=true" width="800">

After completing the form and pressing the submit button, if all the fields were completed and pass the validations, the dynamic upload logo will be enabled and then redirected to a successful submission interface.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.cliente-formulario-envio-formulario.png?raw=true" width="800">

The user will be able to access a help window

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.cliente-formulario-boton-ayuda.png?raw=true" width="800">

If the administrator rejects the documentation due to possible inconsistencies, the user will enter the form again, being able to only modify what was rejected, for example, certain photos:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.cliente-formulario-rechazado.png?raw=true" width="800">


## Admin Side

From the dashboard, you can filter by those operations that are pending review

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.admin-operaciones-pendientes-de-revision.png?raw=true" width="1000">

By clicking on the magnifying glass, you access the "Detail" of the operation. The first header of the accordion contains the documentation information sent by the client, and it is from there that the documentation can be accepted or rejected.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.admin-detalle documentacion cargada.png?raw=true" width="800">

The administrator can open each photo to see it in zoom (or download it) by clicking on the "view image" button on the card:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.admin-doc-vista-previa-imagen.png?raw=true" width="800">

In the event that any photo does not correspond, or its sharpness is not adequate, you can press the "reject photo" button, this will assign a default photo, which is what the client will see when re-entering the link.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.admin-rechazo-foto-formulario.png?raw=true" width="800">

In the event that the client is a company that represents a holder, the administrator may select a "check" to skip the payment and another to skip the turn for vehicle verification.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/2.admin-doc-aprobacion-con-salto.png?raw=true" width="800">



[--- Next --->>>](payment.md#PAYMENT-SYSTEM)
