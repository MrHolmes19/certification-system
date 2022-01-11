# REQUERIMIENTOS DEL CLIENTE

## Comprensión del negocio

El servicio que ofrece nuestro cliente es la elaboración de un informe técnico en el que consta el cambio de tipo de un vehículo (Por ejemplo, para convertir un furgón comercial a uno familiar) y la gestión del certificado emitido por el colegio de ingenieros mecánicos (COPIME). 

El informe es firmado por un ingeniero homologado por dicho instituto. Ambos documentos son necesarios para luego presentar ante el Registro del automotor (DNRPA) y obtener la homologación del cambio para circular legalmente.

## Requerimientos particulares

El cliente ha solicitado que se tengan en cuenta las siguientes características, para la construcción del aplicativo web:

#### Ingreso y acceso
+ Debe contemplar el ingreso tanto de clientes particulares como de empresas que representen a varios clientes (Empresas de repuestos, concesionarias, etc.).
+ Se debe poder ingresar con DNI del titular, CUIT de la empresa (cuando aplique) y Patente del vehículo. También debe poderse ingresar con N° chasis, si el vehículo no posee patente.

#### Pago
+ Debe aceptar todos los medios de pago digitales (Tarjetas, MercadoPago y transferencia bancaria)
+ Debe estar la posibilidad de modificar las tarifas de los servicios y desacoplar otras tarifas preferenciales (con descuento) para empresas.

#### Turnos
+ Sistema para que el cliente pueda reservar un turno para la verificación técnica.
+ Los turnos deben poder sacarse para las próximas 2 semanas como máximo en un horario pre establecido.
+ El administrador debe poder asignar turnos a los clientes y rechazar los ya reservados
+ El administrador debe poder restringir horarios y fechas
+ El sistema debe enviar mail al cliente recordándole el turno un día antes.

#### Informe PDF
+ Con la información cargada por el cliente, debe poder emitirse un informe en PDF en base a una plantilla.
+ El PDF debe contar con: Marca de agua, membrete con logo de la empresa representante y firma digital 

#### Descarga de archivos
+ El cliente debe poder ingresar, una vez estén subidos los archivos, y descargarlos. Además, tendrá 90 días para volver a descargarlos antes de que caduque.


## Propuesta

Tomando en consideración las demandas de nuestro cliente, elaboramos un diagrama conceptual del funcionamiento del negocio con la integración de un aplicativo web, para presentarle nuestra propuesta:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/diag-propuesta-negocio-dark.png?raw=true" width="1000">


[--- Siguiente --->>>](proyect_design.md#DISEÑO-ESTRUCTURAL-DEL-PROYECTO)