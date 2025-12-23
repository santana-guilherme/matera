from decimal import Decimal

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ccb.models.emprestimo import Emprestimo


class EmprestimoTests(APITestCase):
    def setUp(self):
        # Create any necessary test data (e.g., users, objects)
        User = get_user_model()
        self.user = User.objects.create_user(username="noadmin", password="pw")
        self.client.force_login(user=self.user)

    def test_create_account(self):
        """
        Test create Emprestimo object
        """
        url = reverse("emprestimo-list")
        data = {
            "valor_nominal": "10000.00",
            "taxa_juros": 0.0291,
            "banco": "banco-no-admin",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Emprestimo.objects.count(), 1)
        created_emprestimo = Emprestimo.objects.get()
        self.assertEqual(created_emprestimo.cliente.id, self.user.id)
        self.assertEqual(response.data.get("valor_nominal"), data.get("valor_nominal"))
        self.assertEqual(response.data.get("taxa_juros"), data.get("taxa_juros"))
        self.assertEqual(response.data.get("ip"), "127.0.0.1")
        self.assertEqual(response.data.get("banco"), data.get("banco"))
        self.assertEqual(response.data.get("data_quitacao"), None)

    def test_invalid_valor_nominal(self):
        """
        Test create Emprestimo object with invalid valor_nominal
        """
        url = reverse("emprestimo-list")
        data = {
            "valor_nominal": "-5",
            "taxa_juros": 0.0291,
            "banco": "banco-no-admin",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Emprestimo.objects.count(), 0)

    def test_get_saldo_devedor(self):
        """
        Test action saldo_devedor
        """

        empretimo_obj = Emprestimo.objects.create(
            **{
                "valor_nominal": 5000,
                "taxa_juros": 0.023,
                "banco": "nome banco",
                "cliente": self.user,
                "ip": "127.0.0.1",
            }
        )

        url = reverse("emprestimo-saldo-devedor", kwargs={"pk": empretimo_obj.uuid})

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"saldo_devedor": Decimal("6568.67")})
