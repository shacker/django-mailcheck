from django.db import models


class MailCheckMsg(models.Model):
    """For email QA purposes only. Non-production servers save outbound mail
    to the database for QA viewing. Store properties for dummy email objects.
    """

    msg_id = models.CharField(
        max_length=255
    )

    msg_subject = models.CharField(
        blank=True, max_length=255
    )

    msg_from = models.EmailField(
        max_length=200
    )

    msg_to = models.EmailField(
        max_length=200
    )

    msg_date = models.DateTimeField()

    # FIXME: Doesn't yet provide a way to *view* HTML email in browser.
    msg_body = models.TextField(
        blank=True,
        help_text="Can contain both text and html versions of messages (multi-part)",
    )

    def __str__(self) -> str:
        return self.msg_id
