# REQUIREMENTS OF THE CLIENT

## Business understanding

The service offered by our client is the preparation of a technical report that includes the change of type of a vehicle (For example, to convert a commercial van to a family one) and the management of the certificate issued by the College of Mechanical Engineers (COPIME).

The report is signed by an engineer certified by said institute. Both documents are necessary to later present before the Automotive Registry (DNRPA) and obtain the approval of the change to circulate legally.

## Particular requirements

The client has requested that the following characteristics be taken into account for the construction of the web application:

#### Entry and access
+ It must contemplate the entry of both private clients and companies that represent several clients (companies of spare parts, dealers, etc.).
+ You must be able to enter with the ID of the owner, CUIT of the company (when applicable) and Vehicle License. It must also be possible to enter with the chassis number, if the vehicle does not have a license plate.

#### Payment
+ You must accept all digital payment methods (Cards, MercadoPago and bank transfer)
+ There must be the possibility of modifying the rates of the services and decoupling other preferential rates (with discounts) for companies.

#### Shifts
+ System so that the client can reserve a turn for the technical verification.
+ Shifts must be able to be taken out for the next 2 weeks maximum at a pre-established schedule.
+ The administrator must be able to assign shifts to customers and reject those already reserved
+ Admin should be able to restrict times and dates
+ The system must send an email to the client reminding him of the shift one day before.

#### PDF Report
+ With the information uploaded by the client, it must be possible to issue a PDF report based on a template.
+ The PDF must have: Watermark, letterhead with the logo of the representative company and digital signature

#### File Download
+ The client must be able to enter, once the files are uploaded, and download them. Plus, you'll have 90 days to re-download them before they expire.


## Proposal

Taking into consideration the demands of our client, we elaborated a conceptual diagram of the operation of the business with the integration of a web application, to present our proposal:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/diag-propuesta-negocio-dark.png?raw=true" width="1000">


[--- Next --->>>](proyect_design.md#STRUCTURAL-DESIGN-OF-THE-PROJECT)
