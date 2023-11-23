from django.views.generic import TemplateView
from . import models


class ProductTemplateView(TemplateView):
    template_name = 'product/product_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_data'] = models.Product.objects.all()
        return context
