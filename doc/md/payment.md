# SISTEMA DE PAGO

## Lado Cliente

Cuando la operación se encuentra en estado de “Pendiente de pago”, el cliente puede acceder (ya sea desde el Login o desde el link que se le envía por mail) a la interfaz de pago: 

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.cliente-sistema-de-pago.png?raw=true" width="800">

El cliente puede elegir si pagar utilizando la plataforma de Mercado Pago o realizando una transferencia y notificando el pago realizado. En el primer caso, será redireccionado a la página de mercado pago y tendrá la posibilidad de pagar con dinero en cuenta o con tarjetas de débito o crédito.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.cliente-sistema-pago-mercado-pago.png?raw=true" width="800">

Cuando el proceso de pago termine el cliente será redireccionado a la próxima sección.

Si el cliente decide abonar mediante transferencia bancaria, debe hacer click para notificar dicho pago. El administrador será notificado vía mail. El cliente Será redireccionado a una interfaz intermedia, en la que puede decidir volver atrás (Si se arrepintió o si se equivoco al presionar el botón)

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.cliente-sistema-de-pago-pendiente.png?raw=true" width="800">



## Lado Administrador

Los pagos realizados vía plataforma de Mercado Pago, no requerirán intervención del administrador. Cuando en cambio el cliente pague por transferencia bancaria. La operación cambiara al estado de “Pago a revisar”. Desde el dashboard es posible filtrar por este estado.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.admin-filtros.png?raw=true" width="800">

Desde la sección de detalle de operaciones, se podrá aprobar o rechazar el pago, (Si fue por transferencia bancaria) O bien observar cuando, cómo y por qué medio se pagó.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.admin-pago-decision.png?raw=true" width="800">

Si el pago se rechaza, el administrador podrá enviar un mensaje personalizado via mail. La operación volverá a “Pago pendiente” y el usuario volverá a ingresar a la interfaz de pago. El saldo a pagar será la diferencia entre el costo del servicio y lo que el administrador haya registrado en el pago recibido.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.admin-pago-rechazado.png?raw=true" width="800">

Al aprobarse el pago, se anularán las opciones sobre la sección anterior (Formulario) y quedará registrado los datos del pago:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.admin-pago-efectuado.png?raw=true" width="800">
