import logging
import uuid
from decimal import Decimal
from typing import Union

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

logger = logging.getLogger(__name__)


class Emprestimo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#reusable-apps-and-auth-user-model
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    valor_nominal = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(0)]
    )
    taxa_juros = models.FloatField()  # mes
    ip = models.GenericIPAddressField()
    data_solicitacao = models.DateTimeField(auto_now=True)
    banco = models.CharField(max_length=100)
    data_quitacao = models.DateField(null=True)

    class Meta:
        ordering = ["data_solicitacao"]

    def saldo_devedor(self) -> Union[Decimal, None]:
        try:
            total_pago = self.pagamentos.aggregate(models.Sum("valor"))
            total_pago = total_pago.get("valor__sum") or Decimal.from_float(0.0)

            saldo_devedor = (
                self.valor_nominal * Decimal.from_float((1 + self.taxa_juros) ** 12)
            ) - total_pago
            return saldo_devedor.quantize(Decimal("0.00"))
        except Exception as ex:
            logging.exception(
                f"Error calculating saldo_devedor. Ex: {ex}", exc_info=True
            )
            return None
