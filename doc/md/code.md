# ORGANIZATION OF THE CODE

## FOLDER STRUCTURE

Having the following tree of folders and files:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/screenshots/carpeta-codigo.png?raw=true" width="200">

The main folders where the code files are located are the following:


#### Certificates

It contains the fundamental files of the project and of the operation of Django. House inside:

| Carpeta/archivo  | Contenido/Objetivo |
| ------------- | :------------- |
| settings.py:  | It's a file that holds all of Django's general settings. Private configurations, including credentials, are in a separate file, not shared in the repository |
| urls.py:  | global urls |


#### CertificationsApp

It contains information that is shared by the customer section and the administrator section. Contains:

| Folder/file | Content/Objective |
| ------------- | :------------- |
| static: | Folder that contains in turn subfolders with static files (css, Js, images, etc). |
| admin.py: | The classes are defined to display information from the administrator platform that Django offers for the super users of the project. |
| models.py: | Here we define the classes that will make up the tables and respective columns of our database, since we use the ORM provided by Django to abstract from the SQL language. |
| periodic.py: | It contains 2 functions that are triggered periodically: Cleaning of old files and email reminder. |
 

#### Client

Contains everything related to the customer section. House inside:

| Folder/file | Content/Objective |
| ------------- | :------------- |
| templates: | Stores all the .html templates that are rendered during the application. |
| urls.py: | particular urls, where a view is assigned to each one. |
| forms.py: | The classes that the Django modelForm takes for the construction of forms for the interface where the documentation is loaded are defined here. |
| utils.py: | We wrote some functions that we reuse in several instances within the logic of the application, such as sending emails, time conversion, and also part of the redirection logic so as not to bulk up the Login |
| tests.py: | Code used during the development phase to perform unit tests. |
| views.py: | It contains the logic and rendering of all the functionalities and pages. |


#### Dashboard

Contains everything related to the business administrator section. House inside:

| Folder/file | Content/Objective |
| ------------- | :------------- |
| templates: | Stores all the .html templates that are rendered during the application. |
| urls.py: | particular urls, where a view is assigned to each one. |
| forms.py: | The classes that Django's modelForm takes to build forms are defined here. |
| utils.py: | We wrote some functions so as not to bulk up the Dashboard logic in the views.py file. We've introduced here the functions that are fired from periodic.py. |
| Views.py: | It contains the logic and rendering of all the functionalities and pages. |


#### media

In this folder, the folders containing the images that the client uploads on the form page are dynamically generated, as well as the certificate that the administrator uploads in the last stage.

#### doc

Contains the .md files that render this documentation you are reading :)


## STYLES

Styles are mainly given from the html via Bootstrap classes, although we do write some custom styles. All the style files are located inside the “CertificationsApp/static/css” folder:

| Folder/file | Content/Objective |
| ------------- | :------------- |
| clientStyles.css: | Styles for the client section. |
| dashboardStyles.css: | Styles for the admin section. |
| loader.css: | Icon or "spinner" of the loader, when the program is processing a demanding action. |
| reduced-bootstrap.css: | It's a contraction of the Bootstrap file we use during development, which only preserves the classes we use. This contraction is done before going to production with the command “npm run build” which triggers the Liberia function “purgecss”. |
| Minified files: | All files with the “.min.css” extension are minified files, with the aim of reducing the size and improving the performance of the app during rendering. This minification is done with the help of “CSS minifier”. |


## INTERACTIVITY AT THE FRONT FRONT

For the Bootstrap components to work, we use the file “CertificationsApp/static/bootstrap/js/Bootstrap.min.js”.

For custom animations, dynamic styles and other functionality, we use various JS files located within the “CertificationsApp/static/js” folder, namely:

| Folder/file | Content/Objective |
| ------------- | :------------- |
| allModals.js: | Code to enable Bootstrap modals. They are in a separate file since we need to insert dynamic content within them. |
| appointments.js: | It provides the functionality for the shift system, both to select the date with the drop-down calendar button, as well as the schedules. |
| cardsLogic.js: | Describes the logic adopted by the dynamic cards that show the images that the user must upload according to the selected type change. |
| dashboard.js: | It allows displaying a series of functionalities related to the administrator's control panel, such as: Sidebar effects, dynamic titles and real-time search of records. |
| forms.js: | Applies to all pages that have forms, generating different functionalities, such as: Alternation of inputs and legends in the Login form, adding styles to inputs that are automatically generated by Django with the modelForm, and the "loading" symbol when the form is submitted to the Backend. |
| operationDetail.js: | Provides the "operations detail" page with functionalities such as: Block all buttons when the operation is inactive, block inputs when the form is already approved, block approve buttons when an image is rejected, etc. |
| responsive.js: | Applies mobile responsive design to the dashboard interface (Couldn't get hold of Bootstrap classes) |
| speaker.js: | Function to emit a sound when submitting the form that confirms the correct reception of the form.|
| tabs.js: | Assigns a highlight to the selected option on the dashboard navigation bar. |
| types.js: | JSON file with information for each type of vehicle. |
| validations.js: | Validations of inputs on the front side. |


[--- Next --->>>](testing.md#TESTING)
