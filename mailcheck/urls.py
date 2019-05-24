from django.urls import path

from mailcheck.views import (
    index,
    detail,
)

app_name = "mailcheck"

urlpatterns = [
    # Mail check for QA/UAT
    path("", view=index, name="index"),
    path(
        "<int:msg_id>/",
        view=detail,
        name="detail",
    )
]
