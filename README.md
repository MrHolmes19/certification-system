# SISTEMA DE CERTIFICACIONES

<p align="center"> <img src="https://github.com/MrHolmes19/certification-system/blob/main/CertificationsApp/static/CertificationsApp/images/motorhome4.png?raw=true" width="150" align="center"> </p>

## RESUMEN DEL PROYECTO

### Presentación

Esto es una plataforma o sistema web para gestionar el negocio de nuestro cliente (Certificaciones de modificaciones en vehículos para su posterior homologación). Incluye: Carga de documentación, Sistema de pago, sistema de turnos, envío de notificaciones, instrucciones always-on-task de autolimpieza y recordatorio de citas, y un panel de administrador para gestión de tarifas, altas y bajas, consultas y control de las operaciones).

--------------------------------------------------------------------
[***CLICK AQUI PARA ACCEDER A LA APLICACION***](https://app.certificaciones-vehiculares.ar/)
--------------------------------------------------------------------

### Criterios de diseño

La plataforma se ha diseñado de acuerdo al patrón Model View Controller (MVC) o bien Model View Template (MVT). Está dividida en 2 principales secciones: Una para la autogestión del usuario cliente y otra para la gestión del usuario administrador, bajo el aspecto de un tablero de comando. 
Se ha desarrollado todo el código en inglés.

### Tecnologías aplicadas 

El Back-End Fue construido mediante el framework web de Python, Django. Para el Front-end, se ha optado por aprovechar las facilidades del framework Bootstrap para los estilos y funcionalidades básicas y hemos utilizado CSS puro JavaScript Vanilla para estilos y funcionalidades específicas.
La base de datos es SQL y utilizamos MySQL para gestionarla. La aplicación está subido al servidor "PythonAnywhere"


### Autores

Trabajo realizado en colaboración, por:
- Leandro Márquez (lnmarquez19@gmail.com)
- Hernán Monsalvo (monsalvo.h@hotmail.com)


## INDICE DEL CONTENIDO

- [Requerimientos del cliente](doc/md/requirements.md#REQUERIMIENTOS-DEL-CLIENTE)
    + [Comprensión del negocio](doc/md/requirements.md#Comprensión-del-negocio)
    + [Requerimientos particulares](doc/md/requirements.md#Requerimientos-particulares)
    + [Esquema conceptual](doc/md/requirements.md#Propuesta)
- [Diseño estructural del proyecto](doc/md/proyect_design.md#DISEÑO-ESTRUCTURAL-DEL-PROYECTO)
    + [Planificación Base de datos](doc/md/proyect_design.md#resumen-del-proyecto)
    + [Interacción Cliente – Administrador](doc/md/proyect_design.md#Interaccion-Cliente-Administrador)
    + [Estados de cada operación](doc/md/proyect_design.md#Estado-de-la-operación)
- [Funcionalidades del sistema](#el-rincon-de-los-budines)
    + [Carga de documentación](doc/md/login.md#INGRESO-Y-REDIRECCIONAMIENTO)
    + [Sistema de pago](doc/md/payment.md#SISTEMA-DE-PAGO)
    + [Sistema de turnos](doc/md/appointment.md#SISTEMA-DE-TURNOS)
    + [Generación informe PDF](doc/md/pdf_inform.md#GENERACION-DE-INFORME-PDF)
    + [Descarga de archivos](doc/md/certificate.md#CARGA-Y-DESCARGA-DEL-CERTIFICADO)
    + [Notificaciones por mail](doc/md/email_notifications.md#NOTIFICACIONES-POR-MAIL)
    + [Gestión de operaciones inactivas](doc/md/state.md#GESTION-DE-OPERACIONES-INACTIVAS)
    + [Tareas rutinarias](doc/md/always_on_tasks.md#TAREAS-RUTINARIAS)
    + [Tablero de comando](doc/md/dashboard.md#TABLERO-DE-COMANDO)
- [Organización del código](doc/md/code.md#ORGANIZACIÓN-DEL-CÓDIGO)     
    + [Estructura de carpetas](doc/md/code.md#ESTRUCTURA-DE-CARPETAS)
    + [Estilos](doc/md/code.md#ESTILOS)
    + [Interactividad dinámica](doc/md/code.md#INTERACTIVIDAD-EN-EL-FRONT)
- [Testing](doc/md/testing.md#TESTING)
