from django.contrib import admin

from .models import Audiologist, Client

admin.site.disable_action('delete_selected')


class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class AudiologistAdmin(DeleteNotAllowedModelAdmin):
    pass


admin.site.register(Audiologist, AudiologistAdmin)


admin.site.register(Client)
