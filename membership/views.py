from django.http import HttpResponse
from membership.UpdateDB import UpdateMemberDB, UpdateMemberInfo


def index(request):
    return HttpResponse("Hello, world. You're at the membership index.")


def update_db(request):
    updatedb = UpdateMemberDB()
    return HttpResponse('DB Updated with %s members' % updatedb.push_csv_to_db())


def delete_all_members(request):
    updatedb = UpdateMemberDB()
    updatedb.delete_all_members()
    return HttpResponse('All members deleted')

def update_member_info(request):
    member_info = UpdateMemberInfo()
    return HttpResponse('Updated %s members info' % member_info.push_csv_to_db())
