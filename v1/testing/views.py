from django.shortcuts import render
from django.http import HttpResponse
from .models import event


def index(request):
    return HttpResponse("Welcome, you're at the root of the Youthacks Portal")

# Little test to structure event objects as a dict and sent as HTTP response
def events_raw(request):
    events_list_raw = event.objects.order_by("date")
    print("THE NUMBER OF STORED EVENTS IS; ", )
    events_list_parsed = []
    for e in events_list_raw:
        events_list_parsed.append(
            dict({
                "id": e.id,
                "name": e.name,
                "description": e.description,
                "logo": e.logo,
                "address": e.address,
                "date": e.date
            })
        )
    return HttpResponse(events_list_parsed)