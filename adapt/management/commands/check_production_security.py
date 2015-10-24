from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Checks various security settings on the production server'

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
        if admin_user and admin_user.password != "pbkdf2_sha256$20000$TJiPqh3Kc0Z6$RwLPqJllW49P28gvzUHWIegFpdJClRSaVvtOj7U15dI=":
            print("OK")
        else:
            print("WARNING: Password for admin user has not been changed.")