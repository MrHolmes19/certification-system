[*Leer esto en español*](https://github.com/MrHolmes19/certification-system/blob/main/leeme.md)

# CERTIFICATION SYSTEM

<p align="center"> <img src="https://github.com/MrHolmes19/certification-system/blob/main/CertificationsApp/static/CertificationsApp/images/motorhome4.png?raw=true" width="80" align="center"> </p>

## PROJECT SUMMARY

### Presentation

This is a web system to manage our client's business (Certifications of vehicle modifications for subsequent approval). Includes: Documentation loading, payment system, appointment system, sending notifications, always-on-task self-cleaning instructions and appointment reminder, and an administrator panel for managing fees, registrations and cancellations, queries and control of operations).

[*Access the application*](https://app.certificaciones-vehiculares.ar/)


### Design principles

The platform has been designed according to the Model View Controller (MVC) or Model View Template (MVT) pattern. It is divided into 2 main sections: One for client user self-management and another for administrator user management, under the guise of a dashboard. It is totally "responsive designed".
The code has been written entirely in English.

### Applied technologies

The Back-End was built using the Python web framework, Django. For the Front-end, we have chosen to take advantage of the facilities of the Bootstrap framework for basic styles and functionalities and we have used pure CSS and Vanilla Javascript for specific styles and functionalities.
The database is SQL and we use MySQL to manage it. The application is uploaded to the "PythonAnywhere" server.


### Authors

Work done in collaboration, by:
- Leandro Marquez (lnmarquez19@gmail.com)
- Hernán Monsalvo (monsalvo.h@hotmail.com)


## TABLE OF CONTENTS

- [Customer requirements](doc/md/requirements.md#REQUERIMIENTOS-DEL-CLIENTE)
    + [Business Understanding](doc/md/requirements.md#Comprensión-del-negocio)
    + [Particular Requirements](doc/md/requirements.md#Requerimientos-particulares)
    + [Conceptual scheme](doc/md/requirements.md#Propuesta)
- [Structural design of the project](doc/md/proyect_design.md#DISEÑO-ESTRUCTURAL-DEL-PROYECTO)
    + [Database Planning](doc/md/proyect_design.md#resumen-del-proyecto)
    + [Client-Administrator Interaction](doc/md/proyect_design.md#Interaccion-Cliente-Administrador)
    + [Status of each operation](doc/md/proyect_design.md#Estado-de-la-operación)
- [System Features](doc/md/funcionalidades.md#FUNCIONALIDADES-DEL-SISTEMA)
    + [Login & Redirection](doc/md/login.md#INGRESO-Y-REDIRECCIONAMIENTO)
    + [Documentation upload](doc/md/doc_form.md#CARGA-DE-DOCUMENTACION)
    + [Payment system](doc/md/payment.md#SISTEMA-DE-PAGO)
    + [Appointment System](doc/md/appointment.md#SISTEMA-DE-TURNOS)
    + [PDF report generation](doc/md/pdf_inform.md#GENERACION-DE-INFORME-PDF)
    + [File download](doc/md/certificate.md#CARGA-Y-DESCARGA-DEL-CERTIFICADO)
    + [Email notifications](doc/md/email_notifications.md#NOTIFICACIONES-POR-MAIL)
    + [Inactive Operations Management](doc/md/state.md#GESTION-DE-OPERACIONES-INACTIVAS)
    + [Routine tasks](doc/md/always_on_tasks.md#TAREAS-RUTINARIAS)
    + [Dashboard](doc/md/dashboard.md#TABLERO-DE-COMANDO)
- [Code Organization](doc/md/code.md#ORGANIZACIÓN-DEL-CÓDIGO)
    + [Folder structure](doc/md/code.md#ESTRUCTURA-DE-CARPETAS)
    + [Styles](doc/md/code.md#ESTILOS)
    + [Dynamic interactivity](doc/md/code.md#INTERACTIVIDAD-EN-EL-FRONT)
- [Testing](doc/md/testing.md#TESTING)