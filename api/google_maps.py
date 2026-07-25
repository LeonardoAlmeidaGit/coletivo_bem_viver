import requests
from django.conf import settings


def get_coordinates(address: str) -> dict | None:
    """
    Recebe um endereço completo em string e retorna um dicionário
    com latitude e longitude. Retorna None se a API falhar ou
    o endereço não for encontrado.

    Uso: get_coordinates("Rua das Flores, 123, Bairro X, Fortaleza")
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": address,
        "key": settings.GOOGLE_MAPS_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return {
                "lat": location["lat"],
                "lng": location["lng"]
            }

        return None

    except requests.exceptions.RequestException:

        return None


def get_nearby_kitchens(user_address: str, kitchens) -> list:
    """
    Recebe o endereço do usuário e um queryset de cozinhas.
    Retorna a lista de cozinhas ordenadas pela distância em relação
    ao endereço informado, da mais próxima para a mais distante.
    Cozinhas sem coordenadas cadastradas são ignoradas.

    Uso: get_nearby_kitchens("Rua X, 123, Fortaleza", Kitchen.objects.all())
    """
    user_coords = get_coordinates(user_address)

    if not user_coords:

        return list(kitchens)

    def calculate_distance(kitchen) -> float:

        if kitchen.latitude is None or kitchen.longitude is None:
            return float('inf')

        lat_diff = float(kitchen.latitude) - user_coords["lat"]
        lng_diff = float(kitchen.longitude) - user_coords["lng"]
        return (lat_diff ** 2 + lng_diff ** 2) ** 0.5

    return sorted(kitchens, key=calculate_distance)
