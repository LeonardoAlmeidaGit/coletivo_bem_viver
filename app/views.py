from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_refeicoes'] = '25.000'
        context['total_voluntarias'] = '36'
        context['total_cozinhas'] = '16'
        return context
