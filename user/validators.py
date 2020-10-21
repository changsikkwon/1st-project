from django.core.validators   import RegexValidator

def phone_number_validation_function(value): 
    phone_regex = RegexValidator(
        regex   = r'^\+?1?\d{9,15}$',
        message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )

def password_validation_function(value): 
    password_regex = RegexValidator(
        regex   = r'^(?=.*\d)(?=.*[a-zA-Z]).{8,16}$',
        message = "Invalid password format."
        )