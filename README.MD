API Information
# Task 1
- Registration of user and company -

POST api/users/
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
GET api/employees/ (authentication required)

create new employee
POST api/employees/ 
params: 'email', 'first_name', 'last_name', 'password', 'office(optional)'

filtering employees by first name
GET api/employees/?first_name=

filtering employees by last name
GET api/employees/?last_name=

filtering employees by email
GET api/employees/?email=

# Task 4
Worker view/update/delete

View Worker information
GET api/employees/{id}/

Upgrade Worker information
PATCH api/employees/{id}/ (authentication required)
Params: "first_name", "last_name", "office", "password"

Delete Worker
DELETE /employees/{id}/ (authentication required)

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
POST /offices/ (authentication required)
params: 'name','address','country','city','region'

get list of offices 
GET /offices/ (authentication required)

filtering offices by country
GET /offices/?country= (authentication required)

filtering offices by city
GET /offices/?city= (authentication required)

# Task 9
- Office retrieve/update/delete -

get office
GET /offices/{office id}/ (authentication required)

update office
PUT or PATCH /offices/{office id}/
params: 'name', 'address', 'country', 'city', 'region' (authentication required)

delete office
DELETE /offices/{office id}/ (authentication required)

# Task 10
Implemented in Task 4 "Worker view/update/delete"

# Task 11
View my office
GET /office_view/

# Task 12
Vehicle list/create

Get list of company vehicle
GET /vehicle_create_edit/

Create a vehilce
POST /vehicle_create_edit/
params: 'license_plate', 'address', 'country', 'city', 'region' (authentication required)

filtering vehicles by driver name
GET /vehicle_create_edit/?driver={driver name} (authentication required)

filtering offices by office name
GET /vehicle_create_edit/?office={office name} (authentication required)
________________________________
