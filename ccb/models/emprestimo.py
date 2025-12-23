import logging
import uuid
from datetime import datetime
from decimal import Decimal
from typing import Union

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import now

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
    data_solicitacao = models.DateTimeField(default=now)
    banco = models.CharField(max_length=100)
    data_quitacao = models.DateField(null=True)

    class Meta:
        ordering = ["data_solicitacao"]

    def saldo_devedor(self) -> Union[Decimal, None]:
        try:
            months_difference = self._get_month_difference(
                self.data_solicitacao, datetime.now()
            )

            total_pago = self.pagamentos.aggregate(models.Sum("valor"))
            total_pago = total_pago.get("valor__sum") or Decimal.from_float(0.0)

            saldo_devedor = (
                self.valor_nominal
                * Decimal.from_float((1 + self.taxa_juros) ** months_difference)
            ) - total_pago
            return saldo_devedor.quantize(Decimal("0.00"))
        except Exception as ex:
            logging.exception(
                f"Error calculating saldo_devedor. Ex: {ex}", exc_info=True
            )
            return None

    def _get_month_difference(self, start_date, end_date):
        rel_delta = relativedelta(end_date.date(), start_date.date())
        return rel_delta.months + (12 * rel_delta.years)
