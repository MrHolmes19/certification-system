# STRUCTURAL DESIGN OF THE PROJECT

## Database

Considering the following information:

+ Each operation must have inherent information, such as process states, dates, whether it is active or not, etc.
+ Each operation will be linked to a client and a vehicle.
+ Each client may have more than one vehicle and therefore more than one operation in progress.
+ Each vehicle will belong to a client and can only have one active operation at a time.
+ Each company may have several operations in progress.
+ Each vehicle modification (type) may have its individual rate.

The following diagrams were designed:

#### Entity relationship diagram:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/diag-entidad-relacion-dark.png?raw=true" width="1000">

#### Relational model:

Our database contains the following interrelated tables:

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/modelo-relacional-dark.png?raw=true" width="1000">


## Client - Administrator interaction

The following diagram shows the process flow of an operation, and the role played by the client (in turquoise) and the administrator (in yellow).

<img src="https://github.com/MrHolmes19/certification-system/blob/main/doc/diagrams/diag-flujo-de-proceso-dark.png?raw=true" width="1000">


## Status of the operation

Next, the states are expressed from the beginning of the operation to its conclusion, the meaning for both types of user and the reference number to identify it in the process flow.

|States |Customer |Administrator|
| -------------: | -------------: |------------- |
|1 |Documentation sent |Review documentation|
|2 |Modify documentation |Rejected documentation|
|3 |Pending payment |Approved documentation|
|4 |Informed payment |Payment to review|
|5 |Pending shift |Payment confirmed|
|6 |Shift removed |Verification pending|
|7 |Waiting for certificate |Verification passed|
|8 |Certificate Available |Certificate Available|
|9 |Certificate expired |Certificate expired|
|10 |Certificate downloaded |Operation complete|


[--- Next --->>>](functionalities.md#SYSTEM-FUNCTIONALITIES)
