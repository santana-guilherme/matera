from datetime import datetime

from rest_framework import serializers

from ccb.models.emprestimo import Emprestimo
from ccb.serializers.pagamento import PagamentoSerializer


class EmpretimoSerializer(serializers.ModelSerializer):
    ip = serializers.IPAddressField(read_only=True)

    class Meta:
        model = Emprestimo
        fields = "__all__"

    def validate_data_solicitacao(self, value):
        # Usually api timeouts are not bigger than 2 min, so we set this
        # as our tolerance time.
        if not (0 > (datetime.now() - value.date).total_seconds() > 120):
            raise serializers.ValidationError(
                f"A data de solitação deve ser maior ou igual ao dia atual. Valor recebido foi {value}"
            )

    def validate(self, attrs):
        if request := self.context.get("request"):
            attrs["ip"] = request.META.get("REMOTE_ADDR")
        return super().validate(attrs)


class EmprestimoDetailSerializer(EmpretimoSerializer):
    pagamentos = PagamentoSerializer(many=True, read_only=True)
