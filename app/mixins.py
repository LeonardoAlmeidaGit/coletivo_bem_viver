from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class KitchenOwnerMixin(LoginRequiredMixin):
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.kitchen.user != self.request.user:
            raise PermissionDenied()
        return obj
