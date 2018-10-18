from django.db import models
from django.core.validators import RegexValidator


class Member(models.Model):
    card_number = models.IntegerField()
    first_name = models.CharField(max_length=200)
    #TODO: Middle Initial
    last_name = models.CharField(max_length=200)
    #TODO: Age
    address = models.TextField()
    #TODO: Address 2
    city = models.TextField()
    states = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
        ('AS', 'American Samoa'),
        ('DC', 'District of Columbia'),
        ('FM', 'Federated States of Micronesia'),
        ('GU', 'Guam'),
        ('MH', 'Marshall Islands'),
        ('MP', 'Northern Mariana Islands'),
        ('PW', 'Palau'),
        ('PR', 'Puerto Rico'),
        ('VI', 'Virgin Islands'),
        ('AE', 'AE')
    )
    state = models.CharField(max_length=2, choices=states)
    zipcode = models.IntegerField()
    #TODO: Undeliverable
    membership_choices = (
        ('BL', 'Bronze Legacy'),
        ('GL', 'Gold Legacy'),
        ('CO', 'Continuous'),
        ('CU', 'Current Until'),
        ('IL', 'Installment Life'),
        ('LM', 'Life Member'),
        ('NM', 'New Member'),
        ('UP', 'Unpaid')
    )
    membership_type = models.CharField(max_length=2, choices=membership_choices)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class MemberInfo(models.Model):
    card_number = models.ForeignKey(Member, on_delete=models.CASCADE)
    paid_by_post = models.BooleanField()
    paid_by_post_date = models.DateField()
    emailed = models.BooleanField()