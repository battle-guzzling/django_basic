from django.conf.urls import url, include
from AccountManagement.views import *

urlpatterns = [
    url(r"^sign_up", SignUpAPI.as_view()),
    url(r"^sign_in", SignInAPI.as_view()),
]
