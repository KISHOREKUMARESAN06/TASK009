import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

import re

def is_valid_bangladesh_mobile_number(number):
    pattern = r"^(?:\+88|01)[0-9]{9}$"
    return re.match(pattern, number) is not None

import re

def is_valid_usa_telephone_number(number):
    pattern = r"^(?:\+1|1)?[-. (]*[2-9]\d{2}[-). ]*\d{3}[-. ]*\d{4}$"
    return re.match(pattern, number) is not None

import re

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{16}$"
    return re.match(pattern, password) is not None

email = "test@example.com"
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")

mobile_number = "01712345678"
if is_valid_bangladesh_mobile_number(mobile_number):
    print("Valid Bangladesh mobile number")
else:
    print("Invalid Bangladesh mobile number")

telephone_number = "1234567890"
if is_valid_usa_telephone_number(telephone_number):
    print("Valid USA telephone number")
else:
    print("Invalid USA telephone number")

password = "Aa1@password1234"
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")



