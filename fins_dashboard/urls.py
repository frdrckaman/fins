from django.urls import path

from fins_dashboard.views import HomeView

app_name = "fins_dashboard"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]