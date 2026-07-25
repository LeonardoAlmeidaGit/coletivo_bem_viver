from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from . import models, forms
from .models import Kitchen
from api.google_maps import get_coordinates, get_nearby_kitchens


class KitchenOwnerMixin(LoginRequiredMixin):
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied()
        return obj


class KitchenListView(ListView):
    model = models.Kitchen
    template_name = 'kitchen_list.html'
    context_object_name = 'kitchens'

    def get_queryset(self):
        return models.Kitchen.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address = self.request.GET.get('address', '').strip()
        kitchens = self.get_queryset()

        if address:
            result = get_nearby_kitchens(address, kitchens)
            kitchens = result

        kitchens_data = []
        for k in kitchens:
            if k.latitude and k.longitude:
                kitchens_data.append({
                    'name': str(k.name),
                    'address': f'{k.neighborhood}, {k.city}',
                    'lat': float(str(k.latitude)),
                    'lng': float(str(k.longitude)),
                    'url': reverse('kitchen_detail', args=[k.pk]),
                    'status': 'active' if k.status else 'inactive',
                })

        context['kitchens'] = kitchens
        context['kitchens_json'] = kitchens_data
        context['search_address'] = address
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY

        return context


class KitchenCreateView(CreateView):
    model = models.Kitchen
    form_class = forms.KitchenForm
    template_name = 'kitchen_create.html'
    success_url = reverse_lazy('kitchen_detail')

    def get(self, request, *args, **kwargs):
        kitchen = Kitchen.objects.filter(user=request.user).first()

        if kitchen:
            messages.info(request, 'Você já possui uma cozinha cadastrada.')
            return redirect('kitchen_update', pk=kitchen.pk)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        kitchen = Kitchen.objects.filter(user=request.user).first()
        if kitchen:
            return redirect('kitchen_update', pk=kitchen.pk)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        address = f"{form.cleaned_data['address']}, {form.cleaned_data['neighborhood']}, {form.cleaned_data['city']}"
        coordinates = get_coordinates(address)

        if coordinates:
            form.instance.latitude = coordinates['lat']
            form.instance.longitude = coordinates['lng']

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kitchen_detail', kwargs={'pk': self.object.pk})


class KitchenDetailView(DetailView):
    model = models.Kitchen
    template_name = 'kitchen_detail.html'
    context_object_name = 'kitchen'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = self.object.menus.filter(active=True).order_by('-date')
        context['notices'] = self.object.notices.order_by('-created_at')
        context['reviews'] = self.object.reviews.order_by('-created_at')
        return context


class KitchenUpdateView(KitchenOwnerMixin, UpdateView):
    model = models.Kitchen
    form_class = forms.KitchenForm
    template_name = 'kitchen_update.html'
    success_url = reverse_lazy('kitchen_detail')

    def get(self, request, *args, **kwargs):
        kitchen = self.get_object()
        if kitchen.user != request.user and not request.user.is_superuser:
            messages.error(request, 'Você não tem permissão para editar esta cozinha!.')
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        address = f"{form.cleaned_data['address']}, {form.cleaned_data['neighborhood']}, {form.cleaned_data['city']}"
        coordinates = get_coordinates(address)

        if coordinates:
            form.instance.latitude = coordinates['lat']
            form.instance.longitude = coordinates['lng']

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kitchen_detail', kwargs={'pk': self.object.pk})
