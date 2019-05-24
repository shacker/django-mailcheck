# django-mailcheck
Pluggable Django email backend for capturing outbound mail for QA/review purposes.

## What It Is / Who It's For

A common arrangement for larger Django projects is that only the production server sends live email, while test, demo, and staging instances of the site do not. Sure, developers can see outbound emails in the console with:

`EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"`

but what emails are being sent by the test, demo, and staging servers? Emails can be triggered in unexpected ways, which means you might have a QA "black hole." The only way around this would be to set up a mailbox for every test server, and configure each test server to send to that mailbox.

`django-mailcheck` avoids that hassle by capturing outbound email to the database  and allowing it to be viewed at the `/mailcheck` URL, allowing QA teams to review email that *would have been sent* by any running project instance.

**Important:** Mailcheck does *not* send email. It captures it for later viewing, and that's all. Do not use this if you need actual email to be sent from a server to users.

## Installation

Add to your project's `INSTALLED_APPS`:

    "mailcheck",

And migrate your database.

Add to your project's URLs:

    path("mailcheck/", include("mailcheck.urls")),

Add to settings or environment variables:

    EMAIL_BACKEND = "mailcheck.backends.mailcheck.EmailBackend"

Then perform an action on the site that would have triggered an outbound email.

Visit the `/mailcheck` URL.

### Templates

Since it's unlikely the provided templates match your site styles, copy the provided `mailcheck/index.html` and `mailcheck/detail.html` templates from the repo into `templates/mailcheck` in your project.

*IMPORTANT*: The provided views do almost no permission checking, potentially exposing emails that would have been outbound to anyone accessing the `/mailcheck` URL. Since every project has different permissions needs, it is up to you to add appropriate permission checking to your template customizations.


## TODO

- We do not yet correctly display HTML email in the browser
- Naive datetime warnings are issued when storing messages
- Pagination of results
- Auto-pruning of old emails
- More tests

## Running Tests

This app assumes pytest, not unittest.

1. Install pytest
1. From the checkout dir, run `pytest`

## History

*1.0*: Initial release.

