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