# PAYMENT SYSTEM

## Client Side

When the operation is in the status of "Pending payment", the customer can access (either from the Login or from the link sent by email) to the payment interface:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.cliente-sistema-de-pago.png?raw=true" width="800">

The customer can choose whether to pay using the Mercado Pago platform or by making a transfer and notifying the payment made. In the first case, you will be redirected to the payment market page and you will have the possibility to pay with money in your account or with debit and credit cards.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.cliente-sistema-pago-mercado-pago.png?raw=true" width="800">

When the payment process ends, the customer will be redirected to the next section.

In the event that you decide to pay by bank transfer, the customer must click on the button to notify said payment (Which triggers a notification to the administrator) and will be redirected to an intermediate interface, where they can decide to go back (If regretted or if you made a mistake when pressing the button)

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.cliente-sistema-de-pago-pendiente.png?raw=true" width="800">



## Admin Side

Payments made via the Mercado Pago platform will not require administrator intervention. When instead the client pays by bank transfer. The operation will change to the status of "Payment to review". From the dashboard it is possible to filter by this status.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/1.admin-filtros.png?raw=true" width="900">

From the operations detail section, you can approve or reject the payment, (If it was by bank transfer) Or observe when, how and by what means it was paid.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.admin-pago-decision.png?raw=true" width="500">

If the payment is rejected, the administrator can send a personalized message via email. The operation will return to the "Pending payment" status and the user must enter the payment interface again. The balance to be paid will be the difference between the cost of the service and what the administrator has recorded in the payment received, if applicable.

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.admin-pago-rechazado.png?raw=true" width="800">

When the payment is approved, the options on the previous section (Form) will be canceled and the payment data will be registered:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/3.admin-pago-efectuado.png?raw=true" width="800">


[--- Next --->>>](appointment.md#APPOINTMENT-SYSTEM)
