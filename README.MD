API Information
# Task 1
- Registration of user and company -

POST /users/
example:
{
    "email": "_", (required field)
    "first_name": "_", (required field)
    "last_name": "_", (required field)
    "password": "_", (required field)
    "password_repeat":"_", (required field)
    "company": {
        "name": "_", (required field)
        "address": ""
    }
}

# Task 2
 - Login -
POST /token-auth/
Params: 'username', 'password'

# Task 3
getting list of employees
GET /employees/ (authentication required)

create new employee
POST /employees/ 
params: 'email', 'first_name', 'last_name', 'password', 'office(optional)'

filtering employees by first name
GET /employees/?first_name=

filtering employees by last name
GET /employees/?last_name=

filtering employees by email
GET /employees/?email=

# Task 4
Worker view/update/delete

View Worker information
GET /employees/{id}/

Upgrade Worker information
PATCH /company_edit/{id}/ (authentication required)
Params: "first_name", "last_name", "office", "password"

Delete Worker
DELETE /company_edit/{id}/ (authentication required)

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

# Task 12
Vehicle list/create

Get list of company vehicle
GET /vehicle_create_view_list/

filtering vehicles by driver name
GET /vehicle_create_view_list/?driver={driver name} (authentication required)

filtering offices by office name
GET /vehicle_create_view_list/?office={office name} (authentication required)
________________________________
