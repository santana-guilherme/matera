from rest_framework import serializers

from ccb.models.pagamento import Pagamento


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        exclude = ["uuid"]
