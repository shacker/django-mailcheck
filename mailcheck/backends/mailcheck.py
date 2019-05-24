import logging
import threading

from dateutil import parser
from django.core.mail.backends.base import BaseEmailBackend

from mailcheck.models import MailCheckMsg

log = logging.getLogger(__name__)


class EmailBackend(BaseEmailBackend):
    """Email backend that writes messages to database instead of sending them.
    Databased messages are displayed in a view for QA/UAT.

    FIXME(1) msg_date is TZ-naive and throws a warning.
    """

    def __init__(self, *args, **kwargs):
        self._lock = threading.RLock()
        super().__init__(*args, **kwargs)

    def write_message(self, message):
        msg = message.message()

        new_msg = MailCheckMsg.objects.create(
            msg_subject=msg.get("Subject"),
            msg_from=msg.get("From"),
            msg_to=msg.get("To"),
            msg_date=parser.parse(msg.get("Date")),
            msg_body=msg.get_payload(),
            msg_id=msg.get("Message-ID"),
        )
        log.info(msg)
        log.info(f"Outbound email {new_msg.msg_id} saved to mailcheck.")

    def send_messages(self, email_messages):
        """Write all messages to the stream in a thread-safe way."""
        if not email_messages:
            return
        msg_count = 0
        with self._lock:
            try:
                for message in email_messages:
                    self.write_message(message)
                    msg_count += 1
            except Exception:
                if not self.fail_silently:
                    raise
        return msg_count
