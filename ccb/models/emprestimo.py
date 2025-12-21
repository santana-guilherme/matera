import uuid

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Emprestimo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#reusable-apps-and-auth-user-model
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    valor_nominal = models.FloatField(validators=[MinValueValidator(0.0)])
    taxa_juros = models.FloatField()
    ip = models.IPAddressField()
    data_solicitacao = models.DateTimeField(auto_now=True)
    banco = models.CharField(max_length=100)

    class Meta:
        ordering = ["data_solicitacao"]
