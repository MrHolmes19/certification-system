
# SDK of 'Mercado Pago'
import mercadopago

# Adding credentials
sdk = mercadopago.SDK("TEST-3332094717111517-083117-50ddb3f26d4594433d667165a99ad80b-25704844")

# Creating the preference items

preference_data = {
    "items": [
        {
            "title": "Certificación para Cambio de tipo",
            "description": "Verificación visual del vehiculo, elaboración de informe técnico firmado por Ing. mecánico matriculado y entrega de certificado aprobado por el COPYME",
            "quantity": 1,
            "unit_price": 15000,
        }
    ],
    # Returns after payment (Only if the form is not shown trhough a modal in the same page)
    "back_urls": {
        "success": "https://www.tu-sitio/success",
        "failure": "https://www.tu-sitio/failure",
        "pending": "https://www.tu-sitio/pendings"
    },
    "auto_return": "approved"
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]