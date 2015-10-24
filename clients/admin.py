from django.contrib import admin

from .models import Audiologist, Client


class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class AudiologistAdmin(DeleteNotAllowedModelAdmin):
    pass


admin.site.disable_action('delete_selected')

admin.site.site_header = 'Deaf & Hard of Hearing Services - ADAPT'
admin.site.site_title = 'ADAPT'
admin.site.site_url = None
admin.site.index_title = ''

admin.site.register(Audiologist, AudiologistAdmin)
admin.site.register(Client)
