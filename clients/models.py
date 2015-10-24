from django.db import models
import localflavor.us.models as lfmodels

GENDER_CHOICES = [
	('M', 'Male'),
	('F', 'Female'),
	('O', 'Other'),
]

class Client(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	date_of_birth = models.DateField()

	intake_date = models.DateField(auto_now_add=True)

	address = models.TextField(null=True, blank=True)
	city = models.CharField(null=True, blank=True, max_length=64)
	state = lfmodels.USPostalCodeField(null=True, blank=True, default='MI')
	zip_code = lfmodels.USZipCodeField(null=True, blank=True)

	email = models.EmailField(null=True, blank=True)
	phone = lfmodels.PhoneNumberField(null=True, blank=True)

	spouse = models.CharField(null=True, blank=True, max_length=128)

	is_veteran = models.BooleanField(default=True)
	live_alone = models.BooleanField()
	family_size = models.PositiveSmallIntegerField(default=1)

	emergency_contact = models.CharField(null=True, blank=True, max_length=128)
	emergency_phone = lfmodels.PhoneNumberField(null=True, blank=True)
	