from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect



from .models import event, document, staff, staff_signup, attendee, parent, project, waiver, attendee_signup, vote, otp


#def index(request):

@csrf_exempt
@require_http_methods(["GET", "POST"])
def event_json(request):

    # Return all events
    if request.method == "GET":
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
    
    # Create a new event
    elif request.method == "POST":
        event_id = request.POST.get("id")
        name = request.POST.get("name")
        description = request.POST.get("description")
        logo = request.POST.get("logo")
        address = request.POST.get("address")
        date = request.POST.get("date")

        # Validate required fields
        if not all([name, description, logo, address, date]):
            return JsonResponse({
                "status": "error",
                "message": "Missing required fields: name, description, logo, address, date"
            }, status=400, safe=False)

        try:
            target_event = event.objects.get(id=event_id)
            target_event.name = name
            target_event.description = description
            target_event.logo = logo
            target_event.address = address
            target_event.date = date
            target_event.save()

            redirect_url = "/events" + new_event.id
            return redirect(redirect_url)
            
            #return JsonResponse({
            #    "status": "record updated successful",
            #    "id": target_event.id
            #},
            #safe=False
            #)

        except event.DoesNotExist:
            new_event = event.objects.create(
                name = name,
                description = description,
                logo = logo,
                address = address,
                date = date,
                
            )

            redirect_url = "/events" + new_event.id
            return redirect(redirect_url)

            #return JsonResponse({
            #    "status": "creation successful",
            #    "id": new_event.id
            #},
            #safe=False
            #)
            

@require_http_methods(["GET"])
def event_by_eventid_json(request, event_id):
    param = event_id
    list_raw = event.objects.filter(id=param)
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

@require_http_methods(["GET"])
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

@require_http_methods(["GET"])
def document_by_eventid_json(request, event_id):
    param = event_id
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

@require_http_methods(["GET"])
def document_by_documentid_json(request, document_id):
    param = document_id
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

@require_http_methods(["GET"])
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

@require_http_methods(["GET"])
def staff_by_staffid_json(request, staff_id):
    param = staff_id
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

@require_http_methods(["GET"])
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

@require_http_methods(["GET"])
def waiver_by_wavierid_json(request, waiver_id):
    param = waiver_id
    list_raw = waiver.objects.filter(id=param)
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

@require_http_methods(["GET"])
def waiver_by_attendeesignupid_json(request, attendee_signup_id):
    param = attendee_signup_id
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

@require_http_methods(["GET"])
def waiver_by_staffsignupid_json(request, staff_signup_id):
    param = staff_signup_id
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

@require_http_methods(["GET"])
def staff_signup_json(request):
    list_raw = staff_signup.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        waiver_signed = False
        waiver_id = None
        if l.waiver != None:
            waiver_signed = True
            waiver_id = l.waiver.id

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "event_id": l.event.id,
                "staff_id": l.staff.id,
                "staff_name": l.staff.prefered_name,
                "waiver_id": waiver_id,
                "waiver_signed": waiver_signed,
                "role_description": l.role_description,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

@require_http_methods(["GET"])
def parent_json(request): 
    list_raw = parent.objects.order_by("date_created")
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

@require_http_methods(["GET"])
def parent_by_parentid_json(request, parent_id): 
    param = parent_id
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

@require_http_methods(["GET"])
def parent_by_attendeeid_json(request, attendee_id): 
    param = attendee_id
    list_raw = attendee.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.parent.id,
                "prefered_name": l.parent.prefered_name,
                "last_name": l.parent.last_name,
                "email": l.parent.email,
                "date_created": l.parent.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

@require_http_methods(["GET"])
def attendee_json(request): 
    list_raw = attendee.objects.order_by("date_created")
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

@require_http_methods(["GET"])
def attendee_by_attendeeid_json(request, attendee_id): 
    param = attendee_id
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

@require_http_methods(["GET"])
def project_json(request): 
    list_raw = project.objects.order_by("date_created")
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

@require_http_methods(["GET"])
def project_by_project_id_json(request, project_id): 
    param = project_id
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

@require_http_methods(["GET"])
def project_by_attendeesignup_id_json(request, attendee_signup_id): 
    param = attendee_signup_id
    list_raw = attendee_signup.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        list_parsed.append(
            dict({
                "id": l.project.id,
                "event": l.event.name,
                "description": l.project.description,
                "cover_image": l.project.cover_image,
                "repo_link": l.project.repo_link,
                "playable_link": l.project.playable_link,
                "date_created": l.project.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

@require_http_methods(["GET"])
def attendee_signup_json(request):
    list_raw = attendee_signup.objects.order_by("date_created")
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        waiver_signed = False
        waiver_id = None
        if l.waiver != None:
            waiver_signed = True
            waiver_id = l.waiver.id

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "event_id": l.event.id,
                "attendee_id": l.attendee.id,
                "attendee_name": l.attendee.prefered_name,
                "waiver_id": waiver_id,
                "waiver_signed": waiver_signed,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

@require_http_methods(["GET"])
def attendee_signup_by_attendeesignupid_json(request, attendee_signup_id):
    param = attendee_signup_id
    list_raw = attendee_signup.objects.filter(id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        waiver_signed = False
        waiver_id = None
        if l.waiver != None:
            waiver_signed = True
            waiver_id = l.waiver.id

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "event_id": l.event.id,
                "attendee_id": l.attendee.id,
                "attendee_name": l.attendee.prefered_name,
                "waiver_id": waiver_id,
                "waiver_signed": waiver_signed,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

@require_http_methods(["GET"])
def attendee_signup_by_eventid_json(request, event_id):
    param = event_id
    list_raw = attendee_signup.objects.filter(event__id=param)
    print("number of records; ", )
    list_parsed = []
    for l in list_raw:

        waiver_signed = False
        waiver_id = None
        if l.waiver != None:
            waiver_signed = True
            waiver_id = l.waiver.id

        attendee_dict = dict({
            "id": l.attendee.id,
            "first_name": l.attendee.first_name,
            "last_name": l.attendee.last_name,
            "prefered_name": l.attendee.prefered_name,
            "email": l.attendee.email,
            "mobile_number": l.attendee.mobile_number,
            "address": l.attendee.address,
            "dob": l.attendee.dob,
            "medical_info": l.attendee.medical_info,
            "dietary_requirements": l.attendee.dietary_requirements
        })

        list_parsed.append(
            dict({
                "id": l.id,
                "event": l.event.name,
                "event_id": l.event.id,
                "attendee": attendee_dict,
                "waiver_id": waiver_id,
                "waiver_signed": waiver_signed,
                "date_created": l.date_created
            })
        )
    return JsonResponse(list_parsed, safe=False)

@require_http_methods(["GET"])
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

@require_http_methods(["GET"])
def vote_by_projectid_json(request, project_id):
    param = project_id
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

@require_http_methods(["GET"])
def vote_by_attendeesignupid_json(request, attendee_signup_id):
    param = attendee_signup_id
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

@require_http_methods(["GET"])
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

@require_http_methods(["GET"])
def otp_by_attendeeid_json(request, attendee_id):
    param = attendee_id
    list_raw = otp.objects.filter(attendee__id=param)
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

@require_http_methods(["GET"])
def otp_by_staffid_json(request, staff_id):
    param = staff_id
    list_raw = otp.objects.filter(staff__id=param)
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