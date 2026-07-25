from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from kitchens.models import Kitchen
from . import models, forms


class ReviewListView(ListView):
    model = models.Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

    def get_queryset(self):
        kitchen_id = self.kwargs.get('kitchen_id')

        if kitchen_id is not None:
            return models.Review.objects.filter(kitchen_id=kitchen_id)
        return models.Review.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = get_object_or_404(Kitchen, pk=self.kwargs.get('kitchen_id'))
        return context


class ReviewCreateView(CreateView):
    model = models.Review
    template_name = 'review_create.html'
    form_class = forms.ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kitchen_id = self.request.GET.get('kitchen')
        context['kitchen'] = get_object_or_404(Kitchen, pk=kitchen_id)
        return context

    def form_valid(self, form):
        kitchen_id = form.cleaned_data['kitchen'].id
        reviewed_kitchens = self.request.session.get('reviewed_kitchens', [])

        if kitchen_id in reviewed_kitchens:
            form.add_error(None, 'Você já avaliou esta cozinha.')
            return self.form_invalid(form)

        response = super().form_valid(form)
        reviewed_kitchens.append(kitchen_id)
        self.request.session['reviewed_kitchens'] = reviewed_kitchens

        return response

    def get_success_url(self):
        kitchen_id = self.object.kitchen.pk
        return reverse('kitchen_detail', kwargs={'pk': kitchen_id})


class ReviewDetailView(DetailView):
    model = models.Review
    template_name = 'review_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = self.object.kitchen
        return context
