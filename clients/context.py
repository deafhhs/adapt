from . import models


def template_vars(request):
    return {
        'settings': models.Settings.objects.get(),
    }