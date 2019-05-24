import datetime
import pytest
from django.core.mail import send_mail

from mailcheck.models import MailCheckMsg


@pytest.fixture
def mailcheck_setup():
    MailCheckMsg.objects.create(
        msg_id="1234abcd",
        msg_subject="This is a test",
        msg_from="sender@mysite.com",
        msg_to="you@example.com",
        msg_date=datetime.datetime.today(),
        msg_body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
    )


@pytest.mark.django_db
def test_mailcheck_email_stored(mailcheck_setup, settings):
    """When EMAIL_BACKEND is set to mailcheck.backends.mailcheck.EmailBackend,
    as it is on non-production instances, emails are captured to the db for QA viewing."""

    settings.EMAIL_BACKEND = "mailcheck.backends.mailcheck.EmailBackend"
    assert MailCheckMsg.objects.all().count() == 1

    body = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

    send_mail(
        "Subject here",
        body,
        "noreply@energy-solution.net",
        ["foo@example.com"],
        fail_silently=False,
    )

    # Was outbound email captured to database?
    assert MailCheckMsg.objects.all().count() == 2
