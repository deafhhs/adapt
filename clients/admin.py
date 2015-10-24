from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db import models
from django.db.models.fields import CharField, TextField
from django.forms import Textarea, ModelForm
from import_export.admin import ImportExportModelAdmin


from .models import Audiologist
from .models import AudiologistResource
from .models import Client
from .models import ClientResource
from .models import MeetingLog
from .models import MeetingLogResource
from .models import Provider
from .models import ProviderResource
from .models import IncomeSource


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


class ClientIncomeInlineAdmin(admin.TabularInline):
    model = IncomeSource
    can_delete = True
    extra = 1


class MeetingLogInlineAdmin(admin.TabularInline):
    model = MeetingLog
    can_delete = True
    extra = 1


class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource
    list_display = ('first_name', 'last_name', 'intake_date', 'hearing_loss', 'audiologist')  # TODO: cost share
    list_display_links = ('first_name', 'last_name',)
    list_filter = ('intake_date', 'provider', 'audiologist')  # TODO: better date filter, copy from Thrive
    ordering = ('-intake_date',)
    date_hierarchy = 'intake_date'
    search_fields = [f.name for f in Client._meta.local_fields if isinstance(f, (CharField, TextField))]
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(
                attrs={'rows': 3,
                       'cols': 40,
                       'style': 'height: 3.6em;'}
            )
        },
    }
    inlines = (ClientIncomeInlineAdmin,MeetingLogInlineAdmin)

class MeetingLogAdmin(ImportExportModelAdmin):
    resource_class = MeetingLogResource
    list_display = ('client', 'contact_date', 'consultation_time', 'paperwork_time', 'results', 'user')
    list_display_links = ('contact_date',)
    list_filter = ('client', 'contact_date', 'user')
    ordering = ('-contact_date',)
    date_hierarchy = 'contact_date'
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(
                attrs={'rows': 3,
                       'cols': 40,
                       'style': 'height: 3.6em;'}
            )
        },
    }

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
admin.site.register(MeetingLog, MeetingLogAdmin)
