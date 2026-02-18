# Youthacks Portal API Documentation

Base URL: `/testing/`

All endpoints return JSON responses.

---

## Event Endpoints

### List All Events

- **Endpoint:** `GET /event/`
- **Name:** `event_all`
- **Description:** Retrieve all events ordered by date
- **Parameters:** None
- **Response:**

```json
[
  {
    "id": 1,
    "name": "string",
    "description": "string",
    "logo": "url",
    "address": "string",
    "date": "YYYY-MM-DD",
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Event by ID

- **Endpoint:** `GET /event/event_id/<int:event_id>/`
- **Name:** `event_by_eventid`
- **Description:** Retrieve a specific event by ID
- **Parameters:**
  - `event_id` (integer, path) - Event ID
- **Example:** `/event/event_id/1/`
- **Response:** Array with single event object

---

## Document Endpoints

### List All Documents

- **Endpoint:** `GET /document/`
- **Name:** `document_all`
- **Description:** Retrieve all documents ordered by creation date
- **Parameters:** None
- **Response:**

```json
[
  {
    "id": 1,
    "event": 1,
    "path": "url",
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Documents by Event ID

- **Endpoint:** `GET /document/event_id/<str:event_id>/`
- **Name:** `document_by_eventid`
- **Parameters:**
  - `event_id` (string, path) - Event ID
- **Example:** `/document/event_id/1/`

### Get Document by Document ID

- **Endpoint:** `GET /document/document_id/<str:document_id>/`
- **Name:** `document_by_documentid`
- **Parameters:**
  - `document_id` (string, path) - Document ID
- **Example:** `/document/document_id/5/`

---

## Staff Endpoints

### List All Staff

- **Endpoint:** `GET /staff/`
- **Name:** `staff_all`
- **Description:** Retrieve all staff (summary view)
- **Response:**

```json
[
  {
    "id": 1,
    "prefered_name": "string",
    "last_name": "string",
    "email": "string",
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Staff by ID (Detailed)

- **Endpoint:** `GET /staff/staff_id/<str:staff_id>/`
- **Name:** `staff_by_staffid`
- **Parameters:**
  - `staff_id` (string, path) - Staff ID
- **Example:** `/staff/staff_id/3/`
- **Response:**

```json
[
  {
    "id": 1,
    "first_name": "string",
    "last_name": "string",
    "prefered_name": "string",
    "email": "string",
    "mobile_number": "string",
    "address": "string",
    "dob": "YYYY-MM-DD",
    "type": "EXTERNAL|VOLUNTEER|ORGANISER",
    "medical_info": "string",
    "dietary_requirements": "string",
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

---

## Waiver Endpoints

### List All Waivers

- **Endpoint:** `GET /waiver/`
- **Name:** `waiver_all`
- **Response:**

```json
[
  {
    "id": 1,
    "link": "url",
    "date_signed": "YYYY-MM-DD HH:MM:SS",
    "photo_consent": true,
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Waiver by ID

- **Endpoint:** `GET /waiver/waiver_id/<str:waiver_id>/`
- **Name:** `waiver_by_waiverid`
- **Parameters:**
  - `waiver_id` (string, path) - Waiver ID
- **Example:** `/waiver/waiver_id/2/`

### Get Waiver by Attendee Signup ID

- **Endpoint:** `GET /waiver/attendee_signup_id/<str:attendee_signup_id>/`
- **Name:** `waiver_by_attendeesignupid`
- **Parameters:**
  - `attendee_signup_id` (string, path) - Attendee Signup ID
- **Example:** `/waiver/attendee_signup_id/10/`
- **Note:** Returns waiver data for the attendee signup record's associated waiver

### Get Waiver by Staff Signup ID

- **Endpoint:** `GET /waiver/staff_signup_id/<str:staff_signup_id>/`
- **Name:** `waiver_by_staffsignupid`
- **Parameters:**
  - `staff_signup_id` (string, path) - Staff Signup ID
- **Example:** `/waiver/staff_signup_id/7/`
- **Note:** Returns waiver data for the staff signup record's associated waiver

---

## Staff Signup Endpoints

### List All Staff Signups

- **Endpoint:** `GET /staff_signup/`
- **Name:** `staff_signup_all`
- **Response:**

```json
[
  {
    "id": 1,
    "event": "string (event name)",
    "event_id": 1,
    "staff_id": 2,
    "staff_name": "string",
    "waiver_id": 3,
    "waiver_signed": true,
    "role_description": "string",
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

---

## Parent Endpoints

### List All Parents

- **Endpoint:** `GET /parent/`
- **Name:** `parent_all`
- **Response:**

```json
[
  {
    "id": 1,
    "prefered_name": "string",
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "mobile_number": "string",
    "address": "string",
    "dob": "YYYY-MM-DD",
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Parent by ID

- **Endpoint:** `GET /parent/parent_id/<str:parent_id>/`
- **Name:** `parent_by_parentid`
- **Parameters:**
  - `parent_id` (string, path) - Parent ID
- **Example:** `/parent/parent_id/4/`

### Get Parent by Attendee ID

- **Endpoint:** `GET /parent/attendee_id/<str:attendee_id>/`
- **Name:** `parent_by_attendeeid`
- **Parameters:**
  - `attendee_id` (string, path) - Attendee ID
- **Example:** `/parent/attendee_id/15/`
- **Description:** Retrieve parent information for a specific attendee

---

## Attendee Endpoints

### List All Attendees

- **Endpoint:** `GET /attendee/`
- **Name:** `attendee_all`
- **Response:**

```json
[
  {
    "id": 1,
    "prefered_name": "string",
    "last_name": "string",
    "email": "string",
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Attendee by ID

- **Endpoint:** `GET /attendee/attendee_id/<str:attendee_id>/`
- **Name:** `attendee_by_attendeeid`
- **Parameters:**
  - `attendee_id` (string, path) - Attendee ID
- **Example:** `/attendee/attendee_id/8/`

---

## Project Endpoints

### List All Projects

- **Endpoint:** `GET /project/`
- **Name:** `project_all`
- **Response:**

```json
[
  {
    "id": 1,
    "event": "string (event name)",
    "description": "string",
    "cover_image": "url",
    "repo_link": "url",
    "playable_link": "url",
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Project by ID

- **Endpoint:** `GET /project/project_id/<str:project_id>/`
- **Name:** `project_by_projectid`
- **Parameters:**
  - `project_id` (string, path) - Project ID
- **Example:** `/project/project_id/6/`

### Get Project by Attendee Signup ID

- **Endpoint:** `GET /project/attendee_signup_id/<str:attendee_signup_id>/`
- **Name:** `project_by_attendeesignupid`
- **Parameters:**
  - `attendee_signup_id` (string, path) - Attendee Signup ID
- **Example:** `/project/attendee_signup_id/12/`
- **Description:** Retrieve project information associated with an attendee signup

---

## Attendee Signup Endpoints

### List All Attendee Signups

- **Endpoint:** `GET /attendee_signup/`
- **Name:** `attendee_signup_all`
- **Response:**

```json
[
  {
    "id": 1,
    "event": "string (event name)",
    "event_id": 1,
    "attendee_id": 5,
    "attendee_name": "string",
    "waiver_id": 3,
    "waiver_signed": true,
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Attendee Signup by ID

- **Endpoint:** `GET /attendee_signup/attendee_signup_id/<str:attendee_signup_id>/`
- **Name:** `attendee_signup_by_attendeesignupid`
- **Parameters:**
  - `attendee_signup_id` (string, path) - Attendee Signup ID
- **Example:** `/attendee_signup/attendee_signup_id/9/`

### Get Attendee Signups by Event ID

- **Endpoint:** `GET /attendee_signup/event_id/<str:event_id>/`
- **Name:** `attendee_signup_by_eventid`
- **Parameters:**
  - `event_id` (string, path) - Event ID
- **Example:** `/attendee_signup/event_id/2/`
- **Description:** Retrieve all attendee signups for a specific event

---

## Vote Endpoints

### List All Votes

- **Endpoint:** `GET /vote/`
- **Name:** `vote_all`
- **Response:**

```json
[
  {
    "id": 1,
    "attendee_name": "string",
    "attendee_signup_id": 9,
    "project_name": "string (project name)",
    "project_id": 3,
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get Votes by Project ID

- **Endpoint:** `GET /vote/project_id/<str:project_id>/`
- **Name:** `vote_by_projectid`
- **Parameters:**
  - `project_id` (string, path) - Project ID
- **Example:** `/vote/project_id/4/`
- **Description:** Retrieve all votes for a specific project

### Get Votes by Attendee Signup ID

- **Endpoint:** `GET /vote/attendee_signup_id/<str:attendee_signup_id>/`
- **Name:** `vote_by_attendeesignupid`
- **Parameters:**
  - `attendee_signup_id` (string, path) - Attendee Signup ID
- **Example:** `/vote/attendee_signup_id/11/`
- **Description:** Retrieve all votes cast by a specific attendee signup

---

## OTP Endpoints

### List All OTPs

- **Endpoint:** `GET /otp/`
- **Name:** `otp_all`
- **Response:**

```json
[
  {
    "id": 1,
    "staff_name": "string",
    "staff_id": 2,
    "attendee_name": "string",
    "attendee_id": 5,
    "date_created": "YYYY-MM-DD HH:MM:SS"
  }
]
```

### Get OTPs by Attendee ID

- **Endpoint:** `GET /otp/attendee_id/<str:attendee_id>/`
- **Name:** `otp_by_attendeeid`
- **Parameters:**
  - `attendee_id` (string, path) - Attendee ID
- **Example:** `/otp/attendee_id/14/`
- **Description:** Retrieve all OTP records for a specific attendee

### Get OTPs by Staff ID

- **Endpoint:** `GET /otp/staff_id/<str:staff_id>/`
- **Name:** `otp_by_staffid`
- **Parameters:**
  - `staff_id` (string, path) - Staff ID
- **Example:** `/otp/staff_id/3/`
- **Description:** Retrieve all OTP records for a specific staff member

---

## Response Format

All endpoints return responses in one of these formats:

### Success (Array of Objects)

```json
[
  {
    /* object 1 */
  },
  {
    /* object 2 */
  }
]
```

### No Results

```json
[]
```

### Date/Time Format

- Dates: `YYYY-MM-DD`
- DateTimes: `YYYY-MM-DD HH:MM:SS`

### Boolean Values

- `true` or `false` (lowercase)

---

## Testing Examples

```bash
# Get all events
curl http://localhost:8000/testing/event/

# Get specific event
curl http://localhost:8000/testing/event/event_id/1/

# Get attendee signups for event 2
curl http://localhost:8000/testing/attendee_signup/event_id/2/

# Get staff member details
curl http://localhost:8000/testing/staff/staff_id/1/

# Get votes for project 3
curl http://localhost:8000/testing/vote/project_id/3/
```
