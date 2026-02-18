from .models import staff, attendee, otp
import re

# Handle one-time password related queries
class otpManager():

    @classmethod
    def parameter_sanitisation(*parameters):
        # Pattern for string escaping
        sql_injection_pattern = re.compile(r"(')|(''|'')|(--)|(#)|(--)|(;)")
        # Check for matches against pattern
        for parameter in parameters:
            # Throw error if invalid pattern detected
            if bool(sql_injection_pattern.search(parameter)) == True:
                raise ValueError("An inputted parameter contained a disallowed character")
            else:
                return None

    # Fetch prefered name from database
    def get_prefered_name(self, staff_email: str):

        try:
            self.parameter_sanitisation(staff_email)
        except Exception as e:
            print("An error occured: ", e)

        record = staff.objects.get(email=staff_email)
        return record.prefered_name
    
    # Fetch staff_id from database
    def get_staff_id(self, staff_email: str):
        try:
            self.parameter_sanitisation(staff_email)
        except Exception as e:
            print("An error occured: ", e)
        
        record = staff.objects.get(email=staff_email)
        return record.id

    # Insert secret key into otp table
    def insert_secret_key(
            self,
            staff_email: str, 
            secret: str, 
            expiry: int
            ):
        
        try:
            self.parameter_sanitisation(staff_email, secret, expiry)
        except Exception as e:
            print("An error occured: ", e)

        new_otp = otp(
            staff=(staff.objects.get(email=staff_email)),
            login_type = "STAFF_LOGIN",
            token=secret,
            expiry=expiry
                      )
        new_otp.save()

    # Fetch token from otp table
    def fetch_token(self, staff_email: str):

        try:
            self.parameter_sanitisation(staff_email)
        except Exception as e:
            print("An error occured: ", e)

        staff_record = staff.objects.get(email=staff_email)
        otp_record = otp.objects.get(staff__id=staff_record.id)
        return otp_record.token
        
    # Fetch expiry from organiser_auth table
    def fetch_secret_expiry(self, staff_email: str):
        
        try:
            self.parameter_sanitisation(staff_email)
        except Exception as e:
            print("An error occured: ", e)

        staff_record = staff.objects.get(email=staff_email)
        otp_record = otp.objects.get(staff__id=staff_record.id)
        return otp_record.expiry
        
testManager = otpManager()
testManager.get_organiser_id("poolds@proton.me")