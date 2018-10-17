from django.http import HttpResponse
from membership.UpdateDB import UpdateDB


def index(request):
    return HttpResponse("Hello, world. You're at the membership index.")


def update_db(request):
    updatedb = UpdateDB()
    return HttpResponse('DB Updated with %s members' % updatedb.push_csv_to_db())
