import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from mailcheck.models import MailCheckMsg
from rules.contrib.views import permission_required


def index(request: HttpRequest) -> HttpResponse:
    """For non-production instances only - allows viewing outbound email logs.
    This view exists for use by QA/UAT only - not for normal site users.

    FIXME(1) Add pagination of results.
    FIXME(1) Add auto-pruning (auto-delete messages older than n days).
    """

    threshold = 60  # Exclude emails older than this many days
    ago = datetime.timedelta(days=threshold)
    today = datetime.datetime.today()
    emails = MailCheckMsg.objects.filter(msg_date__gte=today - ago).order_by("-msg_date")

    return render(
        request, "mailcheck/index.html", context={"emails": emails, "threshold": threshold}
    )


def detail(request: HttpRequest, msg_id: int) -> HttpResponse:
    """View single mailcheck message.
    This view exists for use by QA/UAT only - not for normal site users.
    """

    email = MailCheckMsg.objects.get(id=msg_id)

    return render(request, "mailcheck/detail.html", context={"email": email})
