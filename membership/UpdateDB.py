from membership.models import Member
import csv


class UpdateDB:
    def __int__(self):
        pass

    def push_csv_to_db(self):
        count = 0
        with open('/tmp/data/postquery.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                count += 1
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
        return count
