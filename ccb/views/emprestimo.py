from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ccb.models.emprestimo import Emprestimo
from ccb.serializers.emprestimo import EmprestimoDetailSerializer, EmpretimoSerializer


class EmprestimoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpretimoSerializer
    serializers = {
        "default": EmpretimoSerializer,
        "retrieve": EmprestimoDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action) or self.serializers.get("default")

    def get_queryset(self):
        request_user = self.request.user
        if request_user.is_superuser:
            return Emprestimo.objects.all()
        else:
            return Emprestimo.objects.filter(cliente__id=request_user.id)

    @action(detail=True, methods=["get"])
    def saldo_devedor(self, request, pk=None):
        emprestimo = self.get_object()
        saldo_devedor = emprestimo.saldo_devedor()
        if saldo_devedor is None:
            return Response(
                {"error": "Error calculating saldo devedor"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response({"saldo_devedor": saldo_devedor}, status=status.HTTP_200_OK)
