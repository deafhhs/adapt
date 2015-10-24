from django.db import models
from django.utils.timezone import now
from import_export import resources
import localflavor.us.models as lfmodels

GENDER_CHOICES = [
    'Male',
    'Female',
    'Other'
]

RACE_CHOICES = [
    'Afro. Amer.',
    'Aleut',
    'Asian',
    'Eskimo',
    'Pac. Islander',
    'White',
    'Other',
]

LOSS_CHOICES = [
    'Mild',
    'Medium',
    'Severe',
    'Profound'
]


class Audiologist(models.Model):
    current = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    allowed = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class AudiologistResource(resources.ModelResource):
    class Meta:
        model = Audiologist
        exclude = ('id',)
        export_order = ('name', 'allowed', 'current', 'notes')


class Client(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=10, choices=zip(GENDER_CHOICES, GENDER_CHOICES))
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    intake_date = models.DateField(default=now)

    address = models.TextField(null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=64)
    state = lfmodels.USPostalCodeField(null=True, blank=True, default='MI')
    zip_code = lfmodels.USZipCodeField(null=True, blank=True)
    deliverable = models.BooleanField(default=True)

    email = models.EmailField(null=True, blank=True)
    phone = lfmodels.PhoneNumberField(null=True, blank=True)

    spouse = models.CharField(null=True, blank=True, max_length=128)

    is_veteran = models.BooleanField(default=False)
    lives_alone = models.BooleanField()
    family_size = models.PositiveSmallIntegerField(default=1)

    emergency_contact = models.CharField(null=True, blank=True, max_length=128)
    emergency_phone = lfmodels.PhoneNumberField(null=True, blank=True)

    race = models.CharField(choices=zip(RACE_CHOICES, RACE_CHOICES), max_length=255)
    is_hispanic = models.BooleanField()
    additional_races = models.CharField(max_length=256, null=True, blank=True)

    referrer = models.CharField(null=True, blank=True, max_length=256)

    hearing_loss = models.CharField(choices=zip(LOSS_CHOICES, LOSS_CHOICES), max_length=255)

    aids_requested_left = models.BooleanField()
    aids_requested_right = models.BooleanField()
    equipment_requested = models.BooleanField()

    cost_share_approval = models.DateField(blank=True, null=True)
    cost_share = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    equipment_borrowed = models.TextField(blank=True)

    provider = models.ForeignKey('Provider', blank=True, null=True)
    audient_id = models.CharField(blank=True, null=True, max_length=16)
    provider_auth_sent = models.DateField(blank=True, null=True)
    provider_auth_recv = models.DateField(blank=True, null=True)

    update_meeting = models.DateField(blank=True, null=True)
    renewal = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True)

    signed_client_intake = models.BooleanField()
    signed_disclosure_authorization = models.BooleanField()
    signed_confidentiality_policy = models.BooleanField()
    signed_gross_annual_income = models.BooleanField()
    signed_client_responsibility_fees = models.BooleanField()

    audiologist = models.ForeignKey(Audiologist, limit_choices_to={'current': True}, null=True, blank=True)
    audiologist_referral_date = models.DateField(null=True, blank=True)
    audiologist_appointment_date = models.DateField(null=True, blank=True)
    audiologist_invoiced_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        exclude = ('id',)


class Provider(models.Model):
    name = models.CharField(max_length=32)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider
        exclude = ('id',)
        export_order = ('name',)


SOURCE_CHOICES = [
    'Client',
    'Spouse',
    'Other',
]

INCOME_CHOICES = [
    'Wages',
    'Social Security Statement',
    'Social Security Disability (SSD)',
    'Social Security Income (SSI)',
    "Veteran's Benefits",
    'Retirement Fund (401), IRA',
    'Annuities',
    'Pension Statement',
    'Checking Account Statement',
    'Savings Account Statement',
    'Mutual Fund Statement',
    'Certificate Deposits (CD)',
    'Stocks / Bonds',
]


class IncomeSource(models.Model):
    client = models.ForeignKey(Client)
    source = models.CharField(choices=zip(SOURCE_CHOICES, SOURCE_CHOICES), max_length=255)
    category = models.CharField(choices=zip(INCOME_CHOICES, INCOME_CHOICES), max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('client', 'source', 'category')

    def __str__(self):
        return '{} {} ${}'.format(self.source, self.category, self.amount)