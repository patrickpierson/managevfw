from django.db import models
from django.core.validators import RegexValidator


class Member(models.Model):
    card_number = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    membership_type = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name