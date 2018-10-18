from django.contrib import admin

from .models import Member, MemberInfo


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'address',
        'city',
        'state',
        'zipcode',
        'membership_type',
        'phone_number',
        'email'
    )

class MemberInfoAdmin(admin.ModelAdmin):
    list_display = (
        'card_number',
        'paid_by_post',
        'paid_by_post_date',
        'emailed'
    )

admin.site.register(Member, MemberAdmin)
admin.site.register(MemberInfo, MemberInfoAdmin)
