from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    
    # Event endpoints
    path("event/", views.event_json, name="event_all"),
    path("event/<str:event_id>/", views.event_by_eventid_json, name="event_by_eventid"),
    
    # Document endpoints
    path("document/", views.document_json, name="document_all"),
    path("document/event/<str:event_id>/", views.document_by_eventid_json, name="document_by_eventid"),
    path("document/<str:document_id>/", views.document_by_documentid_json, name="document_by_documentid"),
    
    # Staff endpoints
    path("staff/", views.staff_json, name="staff_all"),
    path("staff/<str:staff_id>/", views.staff_by_staffid_json, name="staff_by_staffid"),
    
    # Waiver endpoints
    path("waiver/", views.waiver_json, name="waiver_all"),
    path("waiver/<str:waiver_id>/", views.waiver_by_wavierid_json, name="waiver_by_waiverid"),
    path("waiver/attendee-signup/<str:attendee_signup_id>/", views.waiver_by_attendeesignupid_json, name="waiver_by_attendeesignupid"),
    path("waiver/staff-signup/<str:staff_signup_id>/", views.waiver_by_staffsignupid_json, name="waiver_by_staffsignupid"),
    
    # Staff Signup endpoints
    path("staff-signup/", views.staff_signup_json, name="staff_signup_all"),
    
    # Parent endpoints
    path("parent/", views.parent_json, name="parent_all"),
    path("parent/<str:parent_id>/", views.parent_by_parentid_json, name="parent_by_parentid"),
    path("parent/attendee/<str:attendee_id>/", views.parent_by_attendeeid_json, name="parent_by_attendeeid"),
    
    # Attendee endpoints
    path("attendee/", views.attendee_json, name="attendee_all"),
    path("attendee/<str:attendee_id>/", views.attendee_by_attendeeid_json, name="attendee_by_attendeeid"),
    
    # Project endpoints
    path("project/", views.project_json, name="project_all"),
    path("project/<str:project_id>/", views.project_by_project_id_json, name="project_by_projectid"),
    path("project/attendee-signup/<str:attendee_signup_id>/", views.project_by_attendeesignup_id_json, name="project_by_attendeesignupid"),
    
    # Attendee Signup endpoints
    path("attendee-signup/", views.attendee_signup_json, name="attendee_signup_all"),
    path("attendee-signup/<str:attendee_signup_id>/", views.attendee_signup_by_attendeesignupid_json, name="attendee_signup_by_attendeesignupid"),
    path("attendee-signup/event/<str:event_id>/", views.attendee_signup_by_eventid_json, name="attendee_signup_by_eventid"),
    
    # Vote endpoints
    path("vote/", views.vote_json, name="vote_all"),
    path("vote/project/<str:project_id>/", views.vote_by_projectid_json, name="vote_by_projectid"),
    path("vote/attendee-signup/<str:attendee_signup_id>/", views.vote_by_attendeesignupid_json, name="vote_by_attendeesignupid"),
    
    # OTP endpoints
    path("otp/", views.otp_json, name="otp_all"),
    path("otp/attendee/<str:attendee_id>/", views.otp_by_attendeeid_json, name="otp_by_attendeeid"),
    path("otp/staff/<str:staff_id>/", views.otp_by_staffid_json, name="otp_by_staffid"),
]