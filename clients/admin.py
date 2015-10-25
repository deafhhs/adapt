from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db import models
from django.db.models.fields import CharField, TextField
from django.forms import Textarea, ModelForm
from import_export.admin import ImportExportModelAdmin
from solo.admin import SingletonModelAdmin

from .models import Audiologist
from .models import AudiologistResource
from .models import Client
from .models import ClientResource
from .models import MeetingLog
from .models import MeetingLogResource
from .models import Provider
from .models import ProviderResource
from .models import IncomeSource
from .models import Settings


standard_textarea = Textarea(attrs={'rows': 3,
                                    'cols': 40,
                                    'style': 'height: 3.6em;'})


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
    formfield_overrides = {
        models.TextField: {
            'widget': standard_textarea,
        },
    }


class ClientIncomeInlineAdmin(admin.TabularInline):
    model = IncomeSource
    can_delete = True
    extra = 1

class MeetingLogInlineAdminForm(ModelForm):
    class Meta:
        model = MeetingLog
        fields = '__all__'
        widgets = {
            'results': standard_textarea,
        }


class MeetingLogInlineAdmin(admin.TabularInline):
    model = MeetingLog
    form = MeetingLogInlineAdminForm
    can_delete = True
    extra = 1


class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource
    list_display = ('last_name', 'first_name', 'intake_date', 'hearing_loss', 'audiologist', 'cost_share', 'cost_share_approval')
    list_display_links = ('last_name', 'first_name',)
    list_filter = ('provider', 'audiologist', 'family_size', 'deliverable', 'hearing_loss',
                   'equipment_requested', 'adaptive_equipment', 'hearing_aid_assistance',
                   'quota_client', 'non_kcsm',
                   'intake_staff', 'data_entry_staff')
    ordering = ('-intake_date',)
    date_hierarchy = 'intake_date'
    search_fields = [f.name for f in Client._meta.local_fields if isinstance(f, (CharField, TextField))]
    formfield_overrides = {
        models.TextField: {
            'widget': standard_textarea,
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
            'widget': standard_textarea,
        },
    }

class ProviderAdmin(ImportExportModelAdmin):
    ordering = ('name',)
    resource_class = ProviderResource
    formfield_overrides = {
        models.TextField: {
            'widget': standard_textarea,
        },
    }


admin.site.disable_action('delete_selected')

admin.site.site_header = 'Deaf & Hard of Hearing Services - ADAPT'
admin.site.site_title = 'ADAPT'
admin.site.site_url = None
admin.site.index_title = ''

admin.site.register(Audiologist, AudiologistAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(MeetingLog, MeetingLogAdmin)
admin.site.register(Settings, SingletonModelAdmin)
