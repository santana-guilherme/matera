from rest_framework import viewsets

from ccb.models.emprestimo import Emprestimo
from ccb.serializers.emprestimo import EmprestimoDetailSerializer, EmpretimoSerializer


class EmprestimoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpretimoSerializer
    serializers = {
        "default": EmpretimoSerializer,
        "retrive": EmprestimoDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action) or self.serializers.get("default")

    def get_queryset(self):
        request_user = self.request.user
        if request_user.is_superuser:
            return Emprestimo.objects.all()
        else:
            return Emprestimo.objects.filter(client=request_user)
