from django.http import HttpResponse
from membership.models import Member
import csv

def index(request):
    return HttpResponse("Hello, world. You're at the membership index.")


def update_db(request):
    with open('/tmp/data/postquery.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if 'Card_Number' not in row[0]:
                print('Adding/updating member id %s' % row[0])
                _, created = Member.objects.get_or_create(
                    card_number=row[0],
                    first_name=row[2],
                    last_name=row[4],
                    address=row[11],
                    city=row[14],
                    state=row[15],
                    zipcode=row[16],
                    membership_type=row[8],
                    phone_number=row[19],
                    email=row[20]
                )
    return HttpResponse('DB Updated')
