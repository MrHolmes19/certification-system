# SISTEMA DE CERTIFICACIONES

<p align="center"> <img src="https://github.com/MrHolmes19/certification-system/tree/main/CertificationsApp/static/CertificationsApp/images/motorhome4.png?raw=true" width="150" align="center"> </p>

## RESUMEN DEL PROYECTO

### Presentación

Esto es una plataforma o sistema web para gestionar el negocio de nuestro cliente (Certificaciones de modificaciones en vehículos para su posterior homologación). Incluye: Carga de documentación, Sistema de pago, sistema de turnos, envío de notificaciones, instrucciones always-on-task de autolimpieza y recordatorio de citas, y un panel de administrador para gestión de tarifas, altas y bajas, consultas y control de las operaciones).

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

--------------------------------------------------------------------
[**CLICK AQUI PARA ACCEDER A LA APLICACION**](https://app.certificaciones-vehiculares.ar/)
--------------------------------------------------------------------


## INDICE DEL CONTENIDO

- [Requerimientos del cliente](#el-rincon-de-los-budines)
    + [Comprensión del negocio](#resumen-del-proyecto)
    + [Requerimientos particulares](#resumen-del-proyecto)
    + [Esquema conceptual](#resumen-del-proyecto)
- [Diseño estructural del proyecto](#el-rincon-de-los-budines)
    + [Planificación Base de datos](#resumen-del-proyecto)
    + [Interacción Cliente – Administrador](#resumen-del-proyecto)
    + [Estados de cada operación](#resumen-del-proyecto)
- [Funcionalidades del sistema](#el-rincon-de-los-budines)
    + [Ingreso y redireccionamiento](#Ingreso-y-redireccionamiento)
    + [Carga de documentación](#Carga de documentación)
    + [Sistema de pago](#Sistema de pago)
    + [Sistema de turnos](#Sistema de turnos)
    + [Generación informe PDF](#Generación informe PDF)
    + [Notificaciones por mail](#Notificaciones por mail)
    + [Gestión de operaciones inactivas](#Gestión de operaciones inactivas)
    + [Tareas rutinarias (Always-on tasks)](#Tareas rutinarias (Always-on tasks))
    + [Tablero de comando](#Tablero-de-comando)
- [Organización del código](#Organización del código)     
    + [Estructura de carpetas](#Estructura de carpetas)
    + [Estilos](#Estilos)
    + [Interactividad dinámica](#)
- [Testing](#Testing)
