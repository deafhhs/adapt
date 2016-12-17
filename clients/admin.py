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
from .models import Grantor
from .models import GrantorResource


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


class DateYesNoFilter(SimpleListFilter):
    def lookups(self, request, model_admin):
        return (
            ('y', 'Yes'),
            ('n', 'No'),
        )

    def queryset(self, request, queryset):
        query = {}
        if self.value() == 'y':
            query = {self.field_name + '__isnull': False}
        elif self.value() == 'n':
            query = {self.field_name + '__isnull': True}
        return queryset.filter(**query)


class DeceasedFilter(DateYesNoFilter):
    title = 'Deceased'
    parameter_name = 'deceased'
    field_name = 'date_of_death'


class CostShareApprovedFilter(DateYesNoFilter):
    title = 'Cost Share Approved'
    parameter_name = 'cost_share_approved'
    field_name = 'cost_share_approval'


class UpdateMeetingFilter(DateYesNoFilter):
    title = 'Had Update Meeting'
    parameter_name = 'update_meeting'
    field_name = 'update_meeting'


class ProviderAuthReqFilter(DateYesNoFilter):
    title = 'Provider Auth Requested'
    parameter_name = 'provider_auth_requested'
    field_name = 'provider_auth_requested'


class ProviderAuthRecvFilter(DateYesNoFilter):
    title = 'Provider Auth Rcvd'
    parameter_name = 'provider_auth_received'
    field_name = 'provider_auth_received'


class AudiologistReferredFilter(DateYesNoFilter):
    title = 'Audiologist Referred'
    parameter_name = 'audiologist_referral_date'
    field_name = 'audiologist_referral_date'


class AudiologistApptFilter(DateYesNoFilter):
    title = 'Audiologist Appt Set'
    parameter_name = 'audiologist_appointment_date'
    field_name = 'audiologist_appointment_date'


class AudiologistInvoicedFilter(DateYesNoFilter):
    title = 'Audiologist Invoiced'
    parameter_name = 'audiologist_invoiced_date'
    field_name = 'audiologist_invoiced_date'


class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource
    list_display = ('last_name', 'first_name', 'intake_date', 'last_updated', 'hearing_loss', 'audiologist', 'client_grantors', 'cost_share', 'cost_share_approval')
    list_display_links = ('last_name', 'first_name',)
    list_filter = ('provider', 'audiologist', 'grantors', 'family_size', 'hearing_loss',
                   DeceasedFilter, CostShareApprovedFilter, UpdateMeetingFilter, 'update_meeting',
                   ProviderAuthReqFilter, ProviderAuthRecvFilter,
                   AudiologistReferredFilter, AudiologistApptFilter, AudiologistInvoicedFilter,
                   'equipment_requested', 'adaptive_equipment', 'hearing_aid_assistance',
                   'last_updated',
                   'quota_client', 'deliverable', 'non_kcsm',
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

    readonly_fields = ('id', 'last_updated')
    fieldsets = (
        (None, {
            'fields': (
                'id', 'napis_id',
            )
        }),
        ('Personal Info', {
            'fields': (
                'first_name', 'last_name', 'gender', 'date_of_birth', 'date_of_death',
                'is_veteran', 'lives_alone', 'spouse', 'family_size',
            )
        }),
        ('Contact', {
            'fields': (
                'address', 'city', 'county', 'state', 'zip_code', 'deliverable',
                'email', 'phone',
                'emergency_contact',
                'emergency_phone',
            )
        }),
        ('Notes', {
            'fields': (
                'notes',
            )
        }),
        ('Demographics', {
            'fields': (
                'race', 'is_hispanic',
                'multiracial', 'multiracial_white', 'multiracial_black', 'multiracial_asian', 'multiracial_amind',
            )
        }),
        ('Assistance', {
            'fields': (
                'hearing_loss', 'aids_requested_left', 'aids_requested_right', 'equipment_requested',
                'hearing_assistance', 'adaptive_equipment', 'hearing_aid_assistance',
                'equipment_borrowed',
            )
        }),
        ('Additional Forms', {
            'fields': (
                'proof_of_age', 'signed_client_intake', 'signed_disclosure_authorization',
                'signed_confidentiality_policy', 'signed_gross_annual_income',
                'signed_client_responsibility_fees'
            )
        }),
        ('DHHS', {
            'fields': (
                'intake_date', 'intake_staff', 'data_entry_staff', 'last_updated', 'referrer',
                'update_meeting',
                'cost_share_approval', 'cost_share',
                'quota_client', 'non_kcsm', 'grantors',
                'provider', 'audient_id', 'provider_auth_requested', 'provider_auth_received',
            )
        }),
        ('Audiologist', {
            'fields': (
                'audiologist', 'audiologist_referral_date', 'audiologist_appointment_date', 
                'audiologist_invoiced_date', 'audiologist_invoiced_amount',
            )
        }),
    )

class MeetingLogAdmin(ImportExportModelAdmin):
    resource_class = MeetingLogResource
    list_display = ('client', 'contact_date', 'consultation_time', 'paperwork_time', 'units', 'results', 'user')
    list_display_links = ('contact_date',)
    list_filter = ('client', 'contact_date', 'user')
    ordering = ('-contact_date',)
    date_hierarchy = 'contact_date'
    formfield_overrides = {
        models.TextField: {
            'widget': standard_textarea,
        },
    }
    def units(self, obj):
        return (obj.consultation_time + obj.paperwork_time) / 60


class ProviderAdmin(ImportExportModelAdmin):
    ordering = ('name',)
    resource_class = ProviderResource
    formfield_overrides = {
        models.TextField: {
            'widget': standard_textarea,
        },
    }


class GrantorAdmin(ImportExportModelAdmin):
    ordering = ('name',)
    resource_class = GrantorResource
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
admin.site.register(Grantor, GrantorAdmin)
admin.site.register(MeetingLog, MeetingLogAdmin)
admin.site.register(Settings, SingletonModelAdmin)
