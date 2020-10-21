from django.db               import models

from .validators import (
    phone_number_validation_function,
    password_validation_function
)

class User(models.Model): 
    name         = models.CharField(max_length = 16)
    birthdate    = models.DateField(max_length = 16)
    identifier   = models.CharField(max_length = 50, unique = True)
    password     = models.CharField(max_length = 256, validators = [password_validation_function])
    gender       = models.ForeignKey('Gender', on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 17, validators = [phone_number_validation_function], unique = True)
    email        = models.EmailField(max_length = 254, unique = True)

    class Meta: 
        db_table = "users"

class Gender(models.Model): 
    gender = models.CharField(max_length = 16)

    class Meta: 
        db_table = "genders"

class UserInformation(models.Model): 
    endrolled_giftcard = models.PositiveIntegerField()
    coupon             = models.PositiveIntegerField()
    inquiry_history    = models.PositiveIntegerField()
    user               = models.OneToOneField(User, on_delete = models.CASCADE)

    class Meta: 
        db_table = "user_information"
