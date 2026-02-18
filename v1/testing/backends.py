from django.contrib.auth.backends import BaseBackend
from .models import staff, attendee, otp

class OneTimePasswordBackend(BaseBackend):
    def authenticate(self, request, staff_email=None, otp=None):
        record = staff.objects.get(email=staff_email)
        