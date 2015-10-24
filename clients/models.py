from django.db import models
import localflavor.us.models as lfmodels

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

RACE_CHOICES = [
    ('AA', 'Afro. Amer.'),
    ('Al', 'Aleut'),
    ('As', 'Asian'),
    ('Es', 'Eskimo'),
    ('PI', 'Pac. Islander'),
    ('Wh', 'White'),
    ('O' , 'Other')
]

LOSS_CHOICES = [
    (1, 'Mild'),
    (2, 'Medium'),
    (3, 'Severe'),
    (4, 'Profound')
]


class Audiologist(models.Model):
    current = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    allowed = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


class Client(models.Model):
    audiologist = models.ForeignKey(Audiologist, limit_choices_to={'current': True})
    audiologist_referral_date = models.DateField(null=True)
    audiologist_appointment_date = models.DateField(null=True)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    intake_date = models.DateField(auto_now_add=True)

    address = models.TextField(null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=64)
    state = lfmodels.USPostalCodeField(null=True, blank=True, default='MI')
    zip_code = lfmodels.USZipCodeField(null=True, blank=True)
    deliverable = models.BooleanField(default=True)

    email = models.EmailField(null=True, blank=True)
    phone = lfmodels.PhoneNumberField(null=True, blank=True)

    spouse = models.CharField(null=True, blank=True, max_length=128)

    is_veteran = models.BooleanField(default=False)
    live_alone = models.BooleanField()
    family_size = models.PositiveSmallIntegerField(default=1)

    emergency_contact = models.CharField(null=True, blank=True, max_length=128)
    emergency_phone = lfmodels.PhoneNumberField(null=True, blank=True)

    race = models.CharField(choices=RACE_CHOICES, max_length=2)
    is_hispanic = models.BooleanField()
    additional_races = models.CharField(max_length=256)

    referrer = models.CharField(null=True, blank=True, max_length=256)

    hearing_loss = models.PositiveSmallIntegerField(choices=LOSS_CHOICES)

    aids_requested_left = models.BooleanField()
    aids_requested_right = models.BooleanField()
    equipment_requested = models.BooleanField()

    equipment_borrowed = models.TextField(blank=True)