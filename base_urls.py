from django.urls import include, path

"""
This urlconf exists so we can run tests without an actual Django project
(Django expects ROOT_URLCONF to exist.) This helps the tests remain isolated.
For your project, ignore this file and add to your site's urlconf:

`path('mailcheck/', include('mailcheck.urls')),`
"""

urlpatterns = [path("mailcheck/", include("mailcheck.urls"))]
