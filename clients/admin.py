from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from import_export.admin import ImportExportModelAdmin


from .models import Audiologist
from .models import AudiologistResource
from .models import Client
from .models import ClientResource
from .models import Provider
from .models import ProviderResource


class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    
class AudiologistCurrentFilter(SimpleListFilter):
    '''
    Custom filter that defaults to "current" == True
    '''
    title = 'Status'
    parameter_name = 'current'

    def lookups(self, request, model_admin):
        return (
            ('a', 'All audiologists'),
            ('y', 'Current'),
            ('n', 'Inactive'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'a':
            return queryset.filter()
        url_val_map = {
            'y': True,
            'n': False,
            None: True,
        }
        val = url_val_map[self.value()]
        return queryset.filter(current=val)
    
    def choices(self, cl, *a, **kw):
        yield {
            'selected': self.value() is None or self.value == 'y',
            'query_string': cl.get_query_string({}, [self.parameter_name]),
            'display': 'Current',
        }
        yield {
            'selected': self.value() == 'n',
            'query_string': cl.get_query_string({self.parameter_name: 'n'}, []),
            'display': 'Inactive',
        }
        yield {
            'selected': self.value() == 'a',
            'query_string': cl.get_query_string({self.parameter_name: 'a'}, []),
            'display': 'All',
        }



class AudiologistAdmin(DeleteNotAllowedModelAdmin, ImportExportModelAdmin):
    list_display = ('name', 'allowed', 'current')
    list_filter = (AudiologistCurrentFilter,)
    ordering = ('name',)
    resource_class = AudiologistResource


class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource


class ProviderAdmin(ImportExportModelAdmin):
    resource_class = ProviderResource


admin.site.disable_action('delete_selected')

admin.site.site_header = 'Deaf & Hard of Hearing Services - ADAPT'
admin.site.site_title = 'ADAPT'
admin.site.site_url = None
admin.site.index_title = ''

admin.site.register(Audiologist, AudiologistAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Provider, ProviderAdmin)
