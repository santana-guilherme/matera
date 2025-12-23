from rest_framework import viewsets

from ccb.models.pagamento import Pagamento
from ccb.serializers.pagamento import PagamentoSerializer


class PagamentoViewSet(viewsets.ModelViewSet):
    serializer_class = PagamentoSerializer

    def get_queryset(self):
        request_user = self.request.user
        if request_user.is_superuser:
            return Pagamento.objects.all()
        else:
            return Pagamento.objects.filter(emprestimo__cliente__id=request_user.id)
