# DISEÑO ESTRUCTURAL DEL PROYECTO

## Base de datos

Teniendo en cuenta la siguiente información:

+ Cada operación deberá tener información inherente, como estados del proceso, fechas, si esta activa o no, etc.
+ Cada operación estará vinculada con un cliente y un vehículo.
+ Cada cliente podrá tener más de un vehículo y por lo tanto más de una operación en curso.
+ Cada vehículo pertenecerá a un cliente y solo podrá tener una operación activa a la vez.
+ Cada empresa podrá tener varias operaciones en curso.
+ Cada modificación de vehículo (tipo) podrá tener su tarifa individual.

Se diseñaron los siguientes diagramas:

#### Diagrama Entidad - Relación:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/diag-entidad-relacion-dark.png?raw=true" width="1000">

#### Modelo relacional:

Nuestra base de datos contiene las siguientes tablas interrelacionadas, entre sí:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/modelo-relacional-dark.png?raw=true" width="1000">


## Interaccion Cliente - Administrador

En el siguiente esquema se puede observar el flujo de proceso de una operación, y el rol que ocupa el cliente (En turquesa) y el administrador (En amarillo).

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/diag-flujo-de-proceso-dark.png?raw=true" width="1000">


## Estado de la operación

A continuación, se expresan los estados desde el inicio de la operación hasta su conclusión, el significado para ambos tipos de usuario y el número de referencia para identificarlo en el flujo del proceso

|Estados |Cliente |Administrador|
| -------------: | -------------: |------------- |
|1	|Documentación enviada	|Revisar documentación|
|2	|Modificar documentación	|Documentación rechazada|
|3	|Pago pendiente	|Documentación aprobada|
|4	|Pago informado	|Pago a revisar|
|5	|Turno pendiente	|Pago confirmado|
|6	|Turno sacado	|Verificación pendiente|
|7	|Esperando certificado	|Verificación aprobada|
|8	|Certificado disponible	|Certificado disponible|
|9	|Certificado expirado	|Certificado expirado|
|10	|Certificado descargado	|Operación completa|


[--- Siguiente --->>>](funcionalidades.md#FUNCIONALIDADES-DEL-SISTEMA)