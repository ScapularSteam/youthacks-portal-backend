from django.db import models
from django.utils import timezone

# Create table and object relation mappings for each object
class event(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    logo = models.URLField()
    address = models.CharField(max_length=500)
    date = models.DateField()
    date_created = models.DateTimeField(db_default=timezone.now())

class document(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    path = models.URLField()
    date_created = models.DateTimeField(db_default=timezone.now())

class staff(models.Model):
    # Set options for type field
    STAFF_TYPES = {
        "EXTERNAL" : "External",
        "VOLUNTEER" : "Volunteer",
        "ORGANISER" : "Organiser",
    }
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    prefered_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    dob = models.DateField()
    type = models.CharField(max_length=30, choices=STAFF_TYPES)
    medical_info = models.CharField(max_length=500)
    dietary_requirements = models.CharField(max_length=500)
    date_created = models.DateTimeField(db_default=timezone.now())

class waiver(models.Model):
    link = models.URLField(unique=True)
    date_signed = models.DateTimeField()
    photo_consent = models.BooleanField(default=False)
    date_created = models.DateTimeField(db_default=timezone.now())

class staff_signup(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    staff = models.ForeignKey(staff, unique=True, on_delete=models.CASCADE)
    waiver = models.ForeignKey(waiver, on_delete=models.CASCADE)
    role_description = models.CharField(max_length=500)
    date_created = models.DateTimeField(db_default=timezone.now())

class parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    prefered_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    dob = models.DateField()
    date_created = models.DateTimeField(db_default=timezone.now())

class attendee(models.Model):
    parent = models.ForeignKey(parent, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    prefered_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    dob = models.DateField()
    medical_info = models.CharField(max_length=500)
    dietary_requirements = models.CharField(max_length=500)
    date_created = models.DateTimeField(db_default=timezone.now())

class project(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    cover_image = models.URLField()
    repo_link = models.URLField()
    playable_link = models.URLField()
    date_created = models.DateTimeField(db_default=timezone.now())

class attendee_signup(models.Model):
    STATUS_TYPES = {
        "SIGNED_UP": "Signed Up",
        "CHECKED_IN": "Checked in",
        "SCANNED_IN": "Scanned In",
    }
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(attendee, unique=True, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    waiver = models.ForeignKey(waiver, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_TYPES, default="SIGNED_UP")
    date_created = models.DateTimeField(db_default=timezone.now())

class vote(models.Model):
    attendee_signup = models.ForeignKey(attendee_signup, unique=True, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    date_created = models.DateTimeField(db_default=timezone.now())

class otp(models.Model):
    LOGIN_TYPES = {
        "STAFF_LOGIN": "Staff Login",
        "ATTENDEE_LOGIN": "Attendee Login",
    }
    staff = models.ForeignKey(staff, on_delete=models.CASCADE)
    attendee = models.ForeignKey(attendee, on_delete=models.CASCADE)
    login_type = models.CharField(choices=LOGIN_TYPES)
    token = models.CharField(max_length=500)
    expiry = models.IntegerField()
    date_created = models.DateTimeField(db_default=timezone.now())