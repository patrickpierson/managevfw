from membership.models import Member, MemberInfo
from django.core.exceptions import ObjectDoesNotExist
import csv
import datetime

class UpdateMemberDB:
    def __int__(self):
        pass

    def delete_all_members(self):
        Member.objects.all().delete()

    def get_membership_type(self, member_input):
        if 'Life Member' in member_input:
            member_type = 'LM'
        elif 'Bronze Legacy' in member_input:
            member_type = 'BL'
        elif 'Gold Legacy' in member_input:
            member_type = 'GL'
        elif 'Continuous' in member_input:
            member_type = 'CO'
        elif 'Current Until' in member_input:
            member_type = 'CU'
        elif 'Installment Life' in member_input:
            member_type = 'IL'
        elif 'New Member' in member_input:
            member_type = 'NM'
        elif 'UnPaid' in member_input:
            member_type = 'UP'
        else:
            print('Member Type Unknown: %s' % member_input)
            member_type = 'UK'
        return member_type

    def push_csv_to_db(self):
        count = 0
        with open('/tmp/postquery.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                count += 1
                if 'Card_Number' not in row[0]:
                    print('Checking DB for member id %s' % row[0])
                    _, created = Member.objects.get_or_create(
                        card_number=row[0],
                        first_name=row[2].capitalize(),
                        last_name=row[4].capitalize(),
                        address=row[11],
                        city=row[14],
                        state=row[15],
                        zipcode=row[16],
                        membership_type=self.get_membership_type(row[8]),
                        phone_number=row[19],
                        email=row[20]
                    )
                    if created:
                        print('Updated: %s' % _)
        return count


class UpdateMemberInfo:

    def __init__(self):
        pass

    def push_csv_to_db(self):
        count = 0
        with open('/tmp/memberinfo.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                count += 1
                if 'Card Number' not in row[0]:
                    print('Checking DB for member id %s' % row[0])
                    if 'Yes' in row[1]:
                        pbp = True
                    else:
                        pbp = False
                    if row[3]:
                        emailed_status = True
                    else:
                        emailed_status = False
                    try:
                        m = Member.objects.get(card_number=row[0])
                    except ObjectDoesNotExist as e:
                        print(e)
                        m = False
                    if m:
                        #print(m.__dict__)
                        m.memberinfo_set.create(
                            paid_by_post=pbp,
                            paid_by_post_date=datetime.datetime.strptime(row[2], '%m/%d/%Y').strftime('%Y-%m-%d'),
                            emailed=emailed_status
                        )
                    # _, created = MemberInfo.objects.get_or_create(
                    #     card_number=row[0],
                    #     paid_by_post=pbp,
                    #     paid_by_post_date=datetime.datetime.strptime(row[2], '%m/%d/%Y').strftime('%Y-%m-%d'),
                    #     emailed=emailed_status
                    #
                    # )
                    # if created:
                    #     print('Updated: %s' % _)
        return count
