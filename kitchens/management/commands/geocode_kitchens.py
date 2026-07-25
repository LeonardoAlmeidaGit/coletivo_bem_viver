from django.core.management.base import BaseCommand
from kitchens.models import Kitchen
from api.google_maps import get_coordinates


class Command(BaseCommand):
    help = 'Geocodifica cozinhas sem latitude/longitude'

    def handle(self, *args, **kwargs):
        kitchens = Kitchen.objects.filter(latitude__isnull=True)
        for kitchen in kitchens:
            coords = get_coordinates(kitchen.address)
            if coords:
                kitchen.latitude = coords['lat']
                kitchen.longitude = coords['lng']
                kitchen.save()
                self.stdout.write(f'✓ {kitchen.name} geocodificada')
            else:
                self.stdout.write(f'✗ {kitchen.name} falhou')
