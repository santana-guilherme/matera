import uuid

from django.core.validators import MinValueValidator
from django.db import models

from ccb.models.emprestimo import Emprestimo


class Pagamento(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.DateTimeField(auto_now=True)
    valor = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(0.01)]
    )
    emprestimo = models.ForeignKey(
        Emprestimo, related_name="pagamentos", on_delete=models.CASCADE
    )
