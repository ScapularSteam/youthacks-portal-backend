from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import event, document, staff, staff_signup, attendee, parent, project, waiver, attendee_signup, vote, otp


def index(request):
    return HttpResponse("Welcome, you're at the root of the Youthacks Portal")

def event_json(request):
    list_raw = event.objects.order_by("date")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "name": l.name,
                "description": l.description,
                "logo": l.logo,
                "address": l.address,
                "date": l.date,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def event_by_eventid_json(request):
    param = request.GET.get('event_id', '')
    list_raw = event.objects.get(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "name": l.name,
                "description": l.description,
                "logo": l.logo,
                "address": l.address,
                "date": l.date,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def document_json(request):
    list_raw = document.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.id,
                "path": l.path,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def document_by_eventid_json(request):
    param = request.GET.get('event_id', '')
    list_raw = document.objects.filter(event__id=param) # Double underscore accesses attributes from event
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.id,
                "path": l.path,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def document_by_documentid_json(request):
    param = request.GET.get('document_id', '')
    list_raw = document.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.id,
                "path": l.path,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def staff_json(request):
    list_raw = staff.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "prefered_name": l.prefered_name,
                "last_name": l.last_name,
                "email": l.email,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def staff_by_staffid_json(request):
    param = request.GET.get('staff_id', '')
    list_raw = staff.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "first_name": l.first_name,
                "last_name": l.last_name,
                "prefered_name": l.prefered_name,
                "email": l.email,
                "mobile_number": l.mobile_number,
                "address": l.address,
                "dob": l.dob,
                "type": l.type,
                "medical_info": l.medical_info,
                "dietary_requirements": l.dietary_requirements,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def waiver_json(request):
    list_raw = waiver.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "link": l.link,
                "date_signed": l.date_signed,
                "photo_consent": l.photo_consent,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def waiver_by_wavierid_json(request):
    param = request.GET.get('waiver_id', '')
    list_raw = staff.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.id,
                "link": l.link,
                "date_signed": l.date_signed,
                "photo_consent": l.photo_consent,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def waiver_by_attendeesignupid_json(request):
    param = request.GET.get('attendee_signup_id', '')
    list_raw = attendee_signup.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.waiver.id,
                "link": l.waiver.link,
                "date_signed": l.waiver.date_signed,
                "photo_consent": l.waiver.photo_consent,
                "date_created": l.waiver.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def waiver_by_staffsignupid_json(request):
    param = request.GET.get('staff_signup_id', '')
    list_raw = staff_signup.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:
        list_parsed.append(
            dict({
                "id": l.waiver.id,
                "link": l.waiver.link,
                "date_signed": l.waiver.date_signed,
                "photo_consent": l.waiver.photo_consent,
                "date_created": l.waiver.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def staff_signup_json(request):
    list_raw = staff_signup.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        waiver_signed = False
        if l.waiver.date_created != None:
            waiver_signed = True

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "event_id": l.event.id,
                "staff_id": l.staff.id,
                "staff_name": l.staff.prefered_name,
                "waiver_id": l.waiver.id,
                "waiver_signed": waiver_signed,
                "role_description": l.role_description,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def parent_json(request): 
    list_raw = parent.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "prefered_name": l.prefered_name,
                "first_name": l.first_name,
                "last_name": l.last_name,
                "email": l.email,
                "mobile_number": l.mobile_number,
                "address": l.address,
                "dob": l.dob,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def parent_by_parentid_json(request): 

    param = request.GET.get('parent_id', '')
    list_raw = parent.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "prefered_name": l.prefered_name,
                "last_name": l.last_name,
                "email": l.email,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def parent_by_attendeeid_json(request): 

    param = request.GET.get('attendee_id', '')
    list_raw = attendee.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "prefered_name": l.parent.prefered_name,
                "last_name": l.parent.last_name,
                "email": l.parent.email,
                "date_created": l.parent.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def attendee_json(response): 
    list_raw = attendee.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "prefered_name": l.prefered.name,
                "last_name": l.last_name,
                "email": l.email,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)


def attendee_by_attendeeid_json(request): 
    param = request.GET.get('attendee_id', '')
    list_raw = attendee.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "prefered_name": l.prefered_name,
                "last_name": l.last_name,
                "email": l.email,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def project_json(request): 
    list_raw = project.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "description": l.description,
                "cover_image": l.cover_image,
                "repo_link": l.repo_link,
                "playable_link": l.playable_link,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def project_by_project_id_json(request): 
    param = request.GET.get('project_id', '')
    list_raw = project.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "description": l.description,
                "cover_image": l.cover_image,
                "repo_link": l.repo_link,
                "playable_link": l.playable_link,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def project_by_attendeesignup_id_json(request): 
    param = request.GET.get('attendee_signup_id', '')
    list_raw = attendee_signup.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.event.id,
                "event": l.event.event.name,
                "description": l.event.description,
                "cover_image": l.event.cover_image,
                "repo_link": l.event.repo_link,
                "playable_link": l.event.playable_link,
                "date_created": l.event.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def attendee_signup_json(request):
    list_raw = attendee_signup.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        waiver_signed = False
        if l.waiver.date_created != None:
            waiver_signed = True

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "event_id": l.event.id,
                "attendee_id": l.attendee.id,
                "attendee_name": l.attendee.prefered_name,
                "waiver_id": l.waiver.id,
                "waiver_signed": waiver_signed,
                "date_created": l.date_created
            })
        )

def attendee_signup_by_attendeesignupid_json(request):
    param = request.GET.get('attendee_signup_id', '')
    list_raw = attendee_signup.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        waiver_signed = False
        if l.waiver.date_created != None:
            waiver_signed = True

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "event_id": l.event.id,
                "attendee_id": l.attendee.id,
                "attendee_name": l.attendee.prefered_name,
                "waiver_id": l.waiver.id,
                "waiver_signed": waiver_signed,
                "date_created": l.date_created
            })
        )

def attendee_signup_by_eventid_json(request):
    param = request.GET.get('event_id', '')
    list_raw = attendee_signup.objects.filter(event__id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        waiver_signed = False
        if l.waiver.date_created != None:
            waiver_signed = True

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "event_id": l.event.id,
                "attendee_id": l.attendee.id,
                "attendee_name": l.attendee.prefered_name,
                "waiver_id": l.waiver.id,
                "waiver_signed": waiver_signed,
                "date_created": l.date_created
            })
        )

def vote_json(request):
    list_raw = vote.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "attendee_name": l.attendee_signup.attendee.prefered_name,
                "attendee_signup_id": l.attendee_signup.id,
                "project_name": l.project.name,
                "project_id": l.project.id,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def vote_by_projectid_json(request):
    param = request.GET.get('project_id', '')
    list_raw = vote.objects.filter(project__id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "attendee_name": l.attendee_signup.attendee.prefered_name,
                "attendee_signup_id": l.attendee_signup.id,
                "project_name": l.project.name,
                "project_id": l.project.id,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def vote_by_attendeesignupid_json(request):
    param = request.GET.get('attendee_signup_id', '')
    list_raw = vote.objects.filter(attendee_signup__id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "attendee_name": l.attendee_signup.attendee.prefered_name,
                "attendee_signup_id": l.attendee_signup.id,
                "project_name": l.project.name,
                "project_id": l.project.id,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def otp_json(request):
    list_raw = otp.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "staff_name": l.staff.prefered_name,
                "staff_id": l.staff.id,
                "attendee_name": l.attendee.prefered_name,
                "attendee_id": l.attendee.id,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def otp_by_attendeeid_json(request):
    param = request.GET.get('attendee_id', '')
    list_raw = vote.objects.filter(attendee__id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "attendee_name": l.attendee.prefered_name,
                "attendee_id": l.attendee.id,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

def otp_by_staffid_json(request):
    param = request.GET.get('staff_id', '')
    list_raw = vote.objects.filter(staff__id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.id,
                "attendee_name": l.attendee.prefered_name,
                "attendee_id": l.attendee.id,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)