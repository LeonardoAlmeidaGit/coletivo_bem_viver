from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse
from app.mixins import KitchenOwnerMixin
from kitchens.models import Kitchen
from menus.models import Menu, MenuItem
from . import models, forms


MenuItemFormSet = inlineformset_factory(
    models.Menu,
    models.MenuItem,
    form=forms.MenuItemForm,
    extra=3,
    can_delete=True
)


class MenuListView(ListView):
    model = models.Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'

    def get_queryset(self):
        kitchen_id = self.kwargs.get('kitchen_id')

        if kitchen_id is not None:
            return models.Menu.objects.filter(kitchen_id=kitchen_id)
        return models.Menu.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = get_object_or_404(Kitchen, pk=self.kwargs.get('kitchen_id'))
        return context


class MenuCreateView(LoginRequiredMixin, CreateView):
    model = models.Menu
    template_name = 'menu_create.html'
    form_class = forms.MenuForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = self.request.user.kitchen
        return context

    def form_valid(self, form):
        form.instance.kitchen = self.request.user.kitchen
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('menu_update', kwargs={'pk': self.object.pk})


class MenuUpdateView(KitchenOwnerMixin, UpdateView):
    model = Menu
    template_name = 'menu_update.html'
    form_class = forms.MenuForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = self.request.user.kitchen
        context['items'] = self.object.menu_items.all()
        return context

    def get_success_url(self):
        return reverse('menu_update', kwargs={'pk': self.object.pk})


class MenuDeleteView(KitchenOwnerMixin, DeleteView):
    model = models.Menu
    template_name = 'menu_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen'] = self.request.user.kitchen
        return context

    def get_success_url(self):
        return reverse('menu_list', kwargs={'kitchen_id': self.request.user.kitchen.pk})


class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = forms.MenuItemForm
    template_name = 'menuitem_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_object_or_404(Menu, pk=self.kwargs['menu_pk'])
        context['kitchen'] = self.request.user.kitchen
        return context

    def form_valid(self, form):
        form.instance.menu = get_object_or_404(Menu, pk=self.kwargs['menu_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('menu_update', kwargs={'pk': self.kwargs['menu_pk']})


class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    form_class = forms.MenuItemForm
    template_name = 'menuitem_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_object_or_404(Menu, pk=self.kwargs['menu_pk'])
        context['kitchen'] = self.request.user.kitchen
        return context

    def get_success_url(self):
        return reverse('menu_update', kwargs={'pk': self.kwargs['menu_pk']})


class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'menuitem_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_object_or_404(Menu, pk=self.kwargs['menu_pk'])
        context['kitchen'] = self.request.user.kitchen
        return context

    def get_success_url(self):
        return reverse('menu_update', kwargs={'pk': self.kwargs['menu_pk']})
