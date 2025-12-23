from rest_framework.routers import DefaultRouter

from ccb.views.emprestimo import EmprestimoViewSet
from ccb.views.pagamento import PagamentoViewSet

router = DefaultRouter()
router.register(r"emprestimos", EmprestimoViewSet, basename="emprestimo")
router.register(r"pagamentos", PagamentoViewSet, basename="pagamento")
