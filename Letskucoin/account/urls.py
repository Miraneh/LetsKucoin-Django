from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("positions/", login_required(PositionsView.as_view()), name="positions"),

]