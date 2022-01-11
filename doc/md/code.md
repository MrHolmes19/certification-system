# ORGANIZACIÓN DEL CÓDIGO

## ESTRUCTURA DE CARPETAS

Teniendo el siguiente arbol de carpetas y archivos:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/carpeta-codigo.png?raw=true" width="200">

Las carpetas principales donde se alojan los archivos de código son las siguientes:


#### Certificados

Contiene los archivos fundamentales del proyecto y del funcionamiento de Django. Aloja dentro:

| Carpeta/archivo  | Contenido/Objetivo |
| ------------- | :------------- |
| settings.py:  | Es un archivo que guarda todas las configuraciones generales de Django. Las configuraciones privadas, que incluyen credenciales están en un archivo aparte, no compartido en el repositorio |
| urls.py:  | urls generales |


#### CertificationsApp

Contiene información que es compartida por la sección de clientes y la de administrador. Contiene:

| Carpeta/archivo  | Contenido/Objetivo |
| ------------- | :------------- |
| static:  | Carpeta que contiene a su vez subcarpetas con archivos estáticos (css, Js, imágenes, etc). |
| admin.py:  | Se definen las clases para visualizar información desde la plataforma de administrador que ofrece Django para los super usuarios del proyecto. |
| models.py: | Aquí definimos las clases que conformarán las tablas y respectivas columnas de nuestra base de datos, dado que utilizamos el ORM que provee Django para abstraernos del lenguaje SQL. |
| periodic.py: | Contiene 2 funciones que son las que se disparan periódicamente: Limpieza de archivos viejos y recordatorio de mails. |
 

#### Client

Contiene todo lo relacionado a la sección de cliente. Aloja dentro:

| Carpeta/archivo  | Contenido/Objetivo |
| ------------- | :------------- |
| templates: | Almacena todas las plantillas .html que son renderizadas durante la aplicación. |
| urls.py: | urls particulares, donde se asigna una vista “view” para cada uno. |
| forms.py: | Se definen aquí las clases que toma el modelForm de Django para la construcción de formularios para la interfaz donde se carga la documentación. |
| utils.py: | Escribimos algunas funciones que reutilizamos en varias instancias dentro de la lógica de la aplicación, como el envío de mails, conversión horaria, y también parte de la lógica de redireccionamiento para no abultar la lógica del Login |
| tests.py: | Código utilizado durante la fase de desarrollo para realizar pruebas unitarias. |
| views.py: | Contiene la lógica y el renderizado de todas las funcionalidades y páginas. |


#### Dashboard

Contiene todo lo relacionado a la sección del administrador del negocio. Aloja dentro:

| Carpeta/archivo  | Contenido/Objetivo |
| ------------- | :------------- |
| templates: | Almacena todas las plantillas .html que son renderizadas durante la aplicación. |
| urls.py: | urls particulares, donde se asigna una vista “view” para cada uno. |
| forms.py: | Se definen aquí las clases que toma el modelForm de Django para la construcción de formularios. |
| utils.py: | Escribimos algunas funciones para no abultar la lógica del Dashboard en el archivo views.py. Introdujimos aquí las funciones que se disparan desde periodic.py. |
| Views.py: | Contiene la lógica y el renderizado de todas las funcionalidades y páginas. |


#### Media

En esta carpeta se genera dinámicamente las carpetas que contienen las imágenes que sube el cliente en la página de formulario, así como también el certificado que sube el administrador en la última etapa 

#### doc

Contiene los archivos .md que renderizan esta documentación que estas leyendo :)


## ESTILOS

Los estilos son otorgados principalmente desde el html mediante clases de Bootstrap, aunque nosotros escribimos algunos estilos personalizados. Todos los archivos de estilo se encuentran dentro de la carpeta “CertificationsApp/static/css“:

| Carpeta/archivo  | Contenido/Objetivo |
| ------------- | :------------- |
| clientStyles.css: | Estilos para la sección de cliente. |
| dashboardStyles.css: | Estilos para la sección del administrador. |
| loader.css: | Icono o “spinner” del cargador, cuando el programa se encuentra procesando una acción demandante. |
| reduced-bootstrap.css:  | Es una contracción del archivo de Bootstrap que usamos durante el desarrollo, que conserva solamente las clases que utilizamos. Esta contracción se realiza antes de subir a producción con el comando “npm run build” que dispara la función de la Liberia “purgecss”. |
| Archivos minificados: | Todos los archivos con extensión “.min.css” son archivos minificados, con el objetivo de reducir el tamaño y mejorar el rendimiento de la app durante le renderizado. Este minificado se realiza con ayuda de “CSS minifier”. |


## INTERACTIVIDAD EN EL FRONT

Para el funcionamiento de los componentes de Bootstrap nos servimos del archivo “CertificationsApp/static/bootstrap/js/Bootstrap.min.js”.

Para las animaciones, estilos dinámicos y otras funcionalidades personalizados, nos servimos de varios archivos JS alojados dentro de la carpeta “CertificationsApp/static/js“, a saber:

| Carpeta/archivo  | Contenido/Objetivo |
| ------------- | :------------- |
| allModals.js: | Código para habilitar los modals de Bootstrap. Se encuentran en archivo aparte ya que necesitamos insertar contenido dinámico dentro de los mismos. |
| appointmentes.js: | Provee la funcionalidad para el sistema de turnos, tanto para seleccionar fecha con el botón de calendario desplegable, así como los horarios. |
| cardsLogic.js: | Describe la lógica que adoptan las cartas dinámicas que muestran las imágenes que debe subir el usuario según el cambio de tipo seleccionado. |
| dashboard.js: | Permite desplegar una serie de funcionalidades relativas al panel de control del administrador, como ser: Efectos de la barra lateral, títulos dinámicos y búsqueda en tiempo real de registros. |
| forms.js: | Aplica a todas las páginas que poseen formularios, generando distintas funcionalidades, como por ej: Alternancia de inputs y leyendas en el formulario de Login, agregado de estilos a inputs que se generan automáticamente por Django con el modelForm, y el símbolo de “cargando” cuando se envía el formulario al Backend. |
| operationDetail.js: | Provee a la página de “detalle de operaciones” las funcionalidades como: Bloquear todos los botones cuando la operación está inactiva, bloquear inputs cuando el formulario ya está aprobado, bloquea botones de aprobar ante el rechazo de alguna imagen, etc. |
| responsive.js: | Aplica diseño adaptable a mobile a la interfaz del tablero de comando (No pude hacerse con clases de Bootstrap) |
| speaker.js: | Función para emitir un sonido al enviar el formulario que confirme la recepción correcta del formulario.|
| tabs.js: | Asigna un resaltado a la opción seleccionada de la barra de navegación del tablero de comando. |
| types.js: | Archivo JSON con información de cada tipo de vehículo. |
| validations.js: | Validaciones de inputs del lado del front. |


[--- Siguiente --->>>](testing.md#TESTING)