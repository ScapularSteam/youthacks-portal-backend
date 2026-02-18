# Import email dependencies
from email.message import EmailMessage
import smtplib

# Import SMS dependencies
from twilio.rest import Client

# Import database dependencies
import sqlite3

# Import code generation dependencies
import pyotp
import time
import datetime
import uuid
from .otp_manager import otpManager

# Generate HOTP code
def generate_code(email):

    otp = otpManager()

    # Get organiser_id
    id_raw = db.execute(f"""
        SELECT organiser_id FROM organisers WHERE organiser_email = "{email}"
    """).fetchall()
    organiser_id = str(id_raw[0][0])
    
    # Create HOTP
    secret = pyotp.random_base32()
    hotp = pyotp.HOTP(s=secret)
    
    # Create other values required for record insertion
    auth_id = str(uuid.uuid4())
    organiser_email = email
    expiry = (int(time.time()) + 900)

    try:
        # Store secret key in organiser_auth table along with expiry timestamp (UNIX time since epoch + 900s (15 minutes))
        db.execute("""
            INSERT INTO organiser_auth (auth_id, organiser_id, organiser_email, secret, expiry)
            VALUES (?, ?, ?, ?, ?)
        """, (auth_id, organiser_id, organiser_email, secret, expiry))
        db_con.commit()

    except sqlite3.OperationalError as e:
        db_con.rollback()
        print("Failed to create record:", str(e))
        print("No changes were made to the database")
        return {"message": str(e)}
    
    finally:
        db.close()

    # Return code 
    return hotp.at(0)
    
def verify_code(code, email):
    # Connect to database
    db_con = sqlite3.connect("eventstest2.db")
    db = db_con.cursor()

    # Get secret key
    secret_raw = db.execute(f"""
        SELECT secret FROM organiser_auth WHERE organiser_email = "{email}" 
        ORDER BY expiry DESC
    """).fetchall()
    secret = str(secret_raw[0][0])
    print("the secret is: ", secret)

    # Get expiry timestamp
    expiry_raw = db.execute(f"""
        SELECT expiry FROM organiser_auth WHERE organiser_email = "{email}" 
        ORDER BY expiry DESC
    """).fetchone()
    expiry = int(expiry_raw[0])

    # Validate code against secret key
    hotp = pyotp.HOTP(s=secret)
    cryptographically_valid = hotp.verify(otp=code, counter=0)
    print("is code cryptographically valid? ", cryptographically_valid)

    # Validate code for time validity
    if (int(time.time()) <= expiry):
        timevalid = True
    else:
        timevalid = False
    print("Has code existed for less than 15 minutes? ", timevalid)

    # Evaluate time validity and return if code is valid or not
    if (timevalid == True) and (cryptographically_valid == True):
        return True
    else:
        return False
    
def send_code_sms(phone_number, code):

    account_sid = 'AC1fab0b8b5d01ff70b730c2681d0928bb'
    auth_token = '43c93fb3723cbb1ef74271a1406d9cff'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              from_='+447727893589',
                              body = ("[Youthacks Portal] - Your OTP is: " + code),
                              to = phone_number
                          )
    print(message.sid)

def send_code_email(email, code):

    # AWS SES credentials [Hardcoded for testing, TO-DO: Remove from commit history]
    host = "email-smtp.eu-west-2.amazonaws.com"
    port = 465
    username = "AKIA6GBMCFODSL27EI4D"
    password = "BG9TDI8RpXqMZvEGJMQZ5wRCYK9Lat8Qx8oZCH/q8s5a"
    sender = u"auth@youthacks.org"
    recipient = (email,)

    # Message headers
    msg = EmailMessage()
    msg["From"] = "Youthacks Portal <portal@youthacks.org>"
    msg ["To"] = "poolds@proton.me"
    msg["Subject"] = "[Youthacks Portal TEST] Your one-time password"
    preferred_name = get_preferred_name(email)
    # Plain Text formatted message
    msg.set_content(f"""
    Hi {preferred_name},

    Here's your one-time password to sign in:

    {code}

    Your code will expire 15 minutes from now, or after the code is used.

    Kind regards,
    Youthacks Team

    Didn't request a code? Someone else has likely attempted to use your email to login.
    """)

    # Send message
    s = smtplib.SMTP_SSL(host, port, 'youthacks')
    s.login(username, password)
    s.set_debuglevel(0)
    s.sendmail(sender, recipient, str(msg))

#send_code_email("poolds@proton.me", "123456")
#print(pyotp.random_base32())


one_time_code = generate_code("poolds@proton.me")
send_code_email("poolds@proton.me", one_time_code)
send_code_sms(phone_number="+44 7918 831948", code=one_time_code)

print(one_time_code)
otp = int(input(print("please enter otp:")))
print(verify_code(otp, "poolds@proton.me"))