import uuid

from django.core.validators import MinValueValidator
from django.db import models


class Pagamento(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.DateTimeField(auto_now=True)
    valor = models.FloatField(default=0.0, validators=[MinValueValidator(0.01)])
