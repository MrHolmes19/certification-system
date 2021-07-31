from django.test import TestCase
from CertificationsApp.models import Client, Vehicle, Operation, ModificationsType
from .utils import loginRedirect

# Create your tests here.
# loginRedirect test - new client, existing client new vehicle, existing vehicle new operation, existing operation.
class LoginTestCase(TestCase):
    def setUp(self):
        client_data = {
            "id_number": "35761970",
            "name": "Hernan",
            "surname": "Monsalvo",
            "mail": "monsalvo@hernan.com",
            "phone": "42923866"
        }

        cli1 = Client.objects.create(**client_data)

        modification_data1 = {
            "available_type": "Furgon",
            "caption": "Caja cerrada",
            "fee": 5000
        }
        mod1 = ModificationsType.objects.create(**modification_data1)

        modification_data2 = {
            "available_type": "Furgon Frigorifico",
            "caption": "Caja cerrada con equipo de frio",
            "fee": 8000
        }

        mod2 = ModificationsType.objects.create(**modification_data2)

        vehicle_data = {
            "domain": "AA788VB",
            "brand": "volkswagen",
            "model": "gol",
            "last_type": mod1,
            "chassis_number": "asdfgh123456",
            "engine_number": "VW123456789",
            "owner": cli1
        }

        veh1 = Vehicle.objects.create(**vehicle_data)

        operation_data = {
            "certificate_number": "CERT0001",
            "stage": "doc_sent",
            "id_vehicle": veh1,
            "original_type": mod1,
            "final_type": mod2
        }

        ope = Operation.objects.create(**operation_data)

    def test_vehicle_created(self):
        veh = Vehicle.objects.filter(domain="AA788VB").first()

        self.assertEqual(veh.model, "gol")

    def test_operation_created(self):
        ope = Operation.objects.filter(certificate_number="CERT0001").first()

        self.assertEqual(ope.stage, "doc_sent")

    def test_loginRedirect_new_client(self):

        target = loginRedirect("35769070", "AA111BB")

        self.assertEqual(target, "formulario")

    def test_loginRedirect_new_vehicle(self):

        target = loginRedirect("35761970", "AA111BB")

        self.assertEqual(target, "formulario")

    def test_loginRedirect_new_operation(self):

        target = loginRedirect("35761970", "AA788VB")

        self.assertEqual(target, "formulario-pendiente")