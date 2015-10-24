from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings
import requests

class Command(BaseCommand):
    help = 'Checks various security settings on the production server'

    def add_arguments(self, parser):
        parser.add_argument('check_url',
                            help="The server's address")

    def handle(self, *args, **options):
        print()
        print("Checking that admin user exists ...")
        if User.objects.filter(username='admin').exists():
            print("OK")
        else:
            print("ERROR: User admin does not exist.")
        print()
        print("Checking that admin's password has been changed ...")
        admin_user = User.objects.get(username='admin')
        if admin_user and admin_user.password != \
                "pbkdf2_sha256$20000$TJiPqh3Kc0Z6$RwLPqJllW49P28gvzUHWIegFpdJClRSaVvtOj7U15dI=":
            print("OK")
        else:
            print("WARNING: Password for admin user has not been changed.")
        print()
        print("Checking that DEBUG is turned off ...")
        if not settings.DEBUG:
            print("OK")
        else:
            print("WARNING: DEBUG has not been turned off.")
        print()
        print("Checking HSTS ...")
        r = requests.get(options['check_url'])
        if r.headers.get('Strict-Transport-Security', False):
            print("OK")
        else:
            print("WARNING: HSTS is not enabled.")
        print()
        print("Check that URL is HTTPS ...")
        if r.url.startswith("https"):
            print("OK")
        else:
            print("WARNING: URL did not redirect to HTTPS.")
        print()
        print("Check that SECRET_KEY has been changed ...")
        if settings.SECRET_KEY != 'changeme':
            print("OK")
        else:
            print("WARNING: SECRET_KEY has not been changed.")
