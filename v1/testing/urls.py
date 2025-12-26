from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all-events/", views.events_raw, name="all-events")
]