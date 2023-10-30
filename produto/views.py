from django.views.generic import ListView
from .models import Produto

class ProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs
