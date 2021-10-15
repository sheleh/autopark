API Information

getting list of employees
GET /employees/ (authentication required)

filtering employees by first name
GET /employees/?first_name=

filtering employees by last name
GET /employees/?last_name=

filtering employees by email
GET /employees/?email=

# Task 5
getting company information 
GET /company_view/ (authentication required)

# Task 6
company edit
PATCH /company_edit/ (authentication required)
Params: 'name', 'address'

# Task 7
- profile edit -
get profile information
GET /profile_edit/ (authentication required)

update profile information
PATCH /profile_edit/
Params: 'email', 'first_name', 'last_name', 'password'

# Task 8
- create office & view list of offices & filtering -

create office 
POST /office/ (authentication required)
params: 'name','address','country','city','region'

get list of offices 
GET /office/ (authentication required)

filtering offices by country
GET /office/?country= (authentication required)

filtering offices by city
GET /office/?city= (authentication required)

# Task 9
- Office retrieve/update/delete -

get office
GET /office_edit/{office id}/ (authentication required)

update office
PUT or PATCH /office_edit/{office id}/
params: 'name', 'address', 'country', 'city', 'region' (authentication required)

delete office
DELETE /office_edit/{office id}/ (authentication required)

# Task 10
Implemented in Task 4 "Worker view/update/delete"

# Task 11
View my office
GET /office_view/






________________________________

Get a list of existing users
GET http://127.0.0.1:8000/api/all_users

Create a new user:
POST http://127.0.0.1:8000/api/all_users    required fields = username,  password

Get authentication token
POST http://127.0.0.1:8000/api/auth/    required fields = username,  password

View user information:
GET http://127.0.0.1:8000/api/all_users/id (authentication token required)

Modify user information:
PATCH http://127.0.0.1:8000/api/all_users/id (authentication token required)

Delete user:
DELETE http://127.0.0.1:8000/api/all_users/id (authentication token required)

Get a list of existing groups :
GET http://127.0.0.1:8000/api/all_groups (authentication token required)

Create group:
POST http://127.0.0.1:8000/api/all_groups/	required fields = group_name, group_description (authentication token required)

Modify group information:
PATCH http://127.0.0.1:8000/api/all_groups/id/ (authentication token required)

Delete group:
DELETE  http://127.0.0.1:8000/api/all_groups/id/ (authentication token required)