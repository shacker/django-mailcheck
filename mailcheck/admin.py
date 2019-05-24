from django.contrib import admin

from mailcheck.models import MailCheckMsg


class MailCheckMsgAdmin(admin.ModelAdmin):
    list_display = ("msg_date", "msg_subject", "msg_to")


admin.site.register(MailCheckMsg, MailCheckMsgAdmin)
