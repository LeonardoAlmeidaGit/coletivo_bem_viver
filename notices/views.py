from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from app.mixins import KitchenOwnerMixin
from kitchens.models import Kitchen
from . import models, forms


class NoticeListView(ListView):
    model = models.Notice
    template_name = 'notice_list.html'
    context_object_name = 'notices'
    paginate_by = 10

    def get_queryset(self):
        kitchen_id = self.kwargs.get('kitchen_id')

        if kitchen_id is not None:
            return models.Notice.objects.filter(kitchen_id=kitchen_id)
        return models.Notice.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = get_object_or_404(Kitchen, pk=self.kwargs.get('kitchen_id'))
        return context


class NoticeCreateView(KitchenOwnerMixin, CreateView):
    model = models.Notice
    template_name = 'notice_create.html'
    form_class = forms.NoticeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = self.request.user.kitchen
        return context

    def form_valid(self, form):
        form.instance.kitchen = self.request.user.kitchen
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('notice_list', kwargs={'kitchen_id': self.request.user.kitchen.pk})


class NoticeUpdateView(KitchenOwnerMixin, UpdateView):
    model = models.Notice
    template_name = 'notice_update.html'
    form_class = forms.NoticeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = self.request.user.kitchen
        return context
    
    def get_success_url(self):
        return reverse('notice_list', kwargs={'kitchen_id': self.request.user.kitchen.pk})


class NoticeDeleteView(KitchenOwnerMixin, DeleteView):
    model = models.Notice
    template_name = 'notice_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = self.request.user.kitchen
        return context

    def get_success_url(self):
        return reverse('notice_list', kwargs={'kitchen_id': self.request.user.kitchen.pk})
