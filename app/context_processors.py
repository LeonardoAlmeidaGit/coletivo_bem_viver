def user_kitchen(request):

    context = {
        'user_has_kitchen': False,
        'user_kitchen': None,
    }

    if request.user.is_authenticated and not request.user.is_superuser:
        try:
            context['user_has_kitchen'] = True
            context['user_kitchen'] = request.user.kitchen
        except Exception:
            pass

    return context
