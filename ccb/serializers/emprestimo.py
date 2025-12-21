from datetime import datetime

from rest_framework import serializers
from serializers.pagamento import PagamentoSerializer

from ccb.models.emprestimo import Emprestimo


class EmpretimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        exclude = ["uuid", "pagamentos"]

    def validate_data_solicitacao(self, value):
        # Usually api timeouts are not bigger than 2 min, so we set this
        # as our tolerance time.
        if not (0 > (datetime.now() - value.date).total_seconds() > 120):
            raise serializers.ValidationError(
                f"A data de solitação deve ser maior ou igual ao dia atual. Valor recebido foi {value}"
            )


class EmprestimoDetailSerializer(EmpretimoSerializer):
    pagamentos = PagamentoSerializer(many=True, read_only=True)

    class Meta:
        exclude = ["uuid"]
