from django.db import models
from django.utils.timezone import now
from import_export import resources
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
import localflavor.us.models as lfmodels
from solo.models import SingletonModel


GENDER_CHOICES = [
    'Male',
    'Female',
    'Other'
]

RACE_CHOICES = [
    'White',
    'Black',
    'Asian/Hawaiian/Pacific Islander',
    'American Indian/Eskimo/Aleut',
]

LOSS_CHOICES = [
    'Mild',
    'Moderate',
    'Severe',
    'Profound'
]


class Audiologist(models.Model):
    current = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    allowed = models.TextField(null=True, blank=True,
                               help_text='How many clients are generally accepted and which provider(s)')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/admin/clients/audiologist/{}/".format(self.id)



class AudiologistResource(resources.ModelResource):
    class Meta:
        model = Audiologist
        exclude = ('id',)
        export_order = ('name', 'allowed', 'current', 'notes')


class Provider(models.Model):
    name = models.CharField(max_length=32)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/admin/clients/provider/{}/".format(self.id)


class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider
        exclude = ('id',)
        export_order = ('name',)


class Client(models.Model):
    napis_id = models.CharField(max_length=11, null=True, blank=True, verbose_name="NAPIS ID")
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=10, choices=zip(GENDER_CHOICES, GENDER_CHOICES))
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    intake_date = models.DateField(default=now)
    intake_staff = models.ForeignKey(User, related_name='+')
    data_entry_staff = models.ForeignKey(User, related_name='+')

    address = models.TextField()
    city = models.CharField(max_length=64)
    state = lfmodels.USPostalCodeField(default='MI')
    zip_code = lfmodels.USZipCodeField()
    deliverable = models.BooleanField(default=True, verbose_name='Can accept mail')

    email = models.EmailField(null=True, blank=True)
    phone = lfmodels.PhoneNumberField(null=True, blank=True, verbose_name='Phone number')

    spouse = models.CharField(null=True, blank=True, max_length=128)

    is_veteran = models.BooleanField(default=False, verbose_name='Veteran')
    lives_alone = models.BooleanField()
    family_size = models.PositiveSmallIntegerField(default=1, help_text='Including client')

    emergency_contact = models.CharField(null=True, blank=True, max_length=128, verbose_name='Emergency contact name')
    emergency_phone = lfmodels.PhoneNumberField(null=True, blank=True, verbose_name='Emergency contact phone')

    race = models.CharField(choices=zip(RACE_CHOICES, RACE_CHOICES), max_length=255)
    multiracial = models.BooleanField(verbose_name='Multi-Racial')
    multiracial_white = models.BooleanField(verbose_name='White Multi-Racial')
    multiracial_black = models.BooleanField(verbose_name='Black Multi-Racial')
    multiracial_asian = models.BooleanField(verbose_name='Asian Multi-Racial')
    multiracial_amind = models.BooleanField(verbose_name='American Indian Multi-Racial')
    is_hispanic = models.BooleanField(verbose_name='Is Hispanic')

    referrer = models.CharField(null=True, blank=True, max_length=256)

    hearing_loss = models.CharField(choices=zip(LOSS_CHOICES, LOSS_CHOICES), max_length=255)

    aids_requested_left = models.BooleanField(verbose_name='Hearing aid requested (left)')
    aids_requested_right = models.BooleanField(verbose_name='Hearing aid requested (right)')
    equipment_requested = models.BooleanField()

    ''' SERVICES PROVIDED '''
    hearing_assistance = models.BooleanField()
    adaptive_equipment = models.BooleanField()
    hearing_aid_assistance = models.BooleanField()

    cost_share_approval = models.DateField(blank=True, null=True, verbose_name='Cost share approval date')
    cost_share = models.PositiveIntegerField(blank=True, null=True,
                                             validators=[MinValueValidator(0), MaxValueValidator(100)],
                                             verbose_name='Cost share (%)')

    equipment_borrowed = models.TextField(blank=True)

    provider = models.ForeignKey(Provider, blank=True, null=True)
    quota_client = models.BooleanField()
    update_meeting = models.DateField(blank=True, null=True, verbose_name='Update meeting date')
    audient_id = models.CharField(blank=True, null=True, max_length=16, verbose_name='Audient ID')
    provider_auth_requested = models.DateField(blank=True, null=True)
    provider_auth_received = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True)

    proof_of_age = models.BooleanField()
    signed_client_intake = models.BooleanField()
    signed_disclosure_authorization = models.BooleanField()
    signed_confidentiality_policy = models.BooleanField()
    signed_gross_annual_income = models.BooleanField()
    signed_client_responsibility_fees = models.BooleanField()

    audiologist = models.ForeignKey(Audiologist, limit_choices_to={'current': True}, null=True, blank=True)
    audiologist_referral_date = models.DateField(null=True, blank=True)
    audiologist_appointment_date = models.DateField(null=True, blank=True)
    audiologist_invoiced_date = models.DateField(blank=True, null=True)
    audiologist_invoiced_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                                      validators=[MinValueValidator(0)],
                                                      verbose_name='Audiologist invoiced amount ($)')

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return "/admin/clients/client/{}/".format(self.id)

    @property
    def total_income(self):
        return sum(inc.annual for inc in self.incomesource_set.all())
    



class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'gender', 'date_of_birth',
          'date_of_death', 'intake_date', 'address', 'city', 'state',
          'zip_code', 'deliverable', 'email', 'phone', 'spouse',
          'is_veteran', 'lives_alone', 'family_size',
          'emergency_contact', 'emergency_phone', 'race', 'is_hispanic',
          'additional_races', 'referrer', 'hearing_loss',
          'aids_requested_left', 'aids_requested_right',
          'equipment_requested', 'cost_share_approval', 'cost_share',
          'equipment_borrowed', 'provider__name', 'audient_id',
          'provider_auth_sent', 'provider_auth_recv', 'update_meeting',
          'notes', 'signed_client_intake',
          'signed_disclosure_authorization',
          'signed_confidentiality_policy', 'signed_gross_annual_income',
          'signed_client_responsibility_fees', 'audiologist__name',
          'audiologist_referral_date', 'audiologist_appointment_date',
          'audiologist_invoiced_date')



class MeetingLog(models.Model):
    client = models.ForeignKey(Client)

    contact_date = models.DateField()

    consultation_time = models.PositiveIntegerField(default=15, verbose_name='Consulation time (minutes)')
    paperwork_time = models.PositiveIntegerField(default=15, verbose_name='Paperwork time (minutes)')

    results = models.TextField(blank=True, help_text='Problems, solutions, progress, equipment, etc.')

    user = models.ForeignKey(User)

    def get_absolute_url(self):
        return "/admin/clients/meetinglog/{}/".format(self.id)
    

class MeetingLogResource(resources.ModelResource):
    class Meta:
        model = MeetingLog
        exclude = ('id',)


SOURCE_CHOICES = [
    'Client',
    'Spouse',
    'Other',
]

INCOME_CHOICES_MONTHLY = [
    'Wages',
    'Social Security Statement',
    'Social Security Disability',
    'Social Security Income',
    "Veteran's Benefits",
    'Retirement Fund (401), IRA',
]
INCOME_CHOICES_YEARLY = [
    'Annuities',
    'Pension Statement',
    'Checking Account Statement',
    'Savings Account Statement',
    'Mutual Fund Statement',
    'Certificate Deposits',
    'Stocks / Bonds',
]
INCOME_CHOICES_ALL = INCOME_CHOICES_MONTHLY+INCOME_CHOICES_YEARLY


class IncomeSource(models.Model):
    client = models.ForeignKey(Client)
    source = models.CharField(choices=zip(SOURCE_CHOICES, SOURCE_CHOICES), max_length=255)
    category = models.CharField(
        choices=zip(INCOME_CHOICES_MONTHLY + INCOME_CHOICES_YEARLY,
                    [im + ' (Monthly)' for im in INCOME_CHOICES_MONTHLY] + INCOME_CHOICES_YEARLY),
        max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def annual(self):
        if self.category in INCOME_CHOICES_MONTHLY:
            return self.amount * 12
        else:
            return self.amount

    class Meta:
        unique_together = ('client', 'source', 'category')

    def __str__(self):
        return '{} {} ${}'.format(self.source, self.category, self.amount)


class Settings(SingletonModel):
    income_level_1 = models.IntegerField()
    income_level_2 = models.IntegerField()
    AAA_VendorID = models.IntegerField()
    AAA_VendorSite = models.IntegerField()
    AAA_Region = models.IntegerField()
    AAA_County = models.IntegerField()

    def __str__(self):
        return "Settings"

    class Meta:
        verbose_name = "Settings"


