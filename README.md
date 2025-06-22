# Clinic App 

## Setup

pip install -r requirements.txt
   

python "DB manipulations/TableCreate.py"
python "DB manipulations/DataAdd.py"

uvicorn app:app --reload or docker-compose up -d

http://127.0.0.1:8000

## Usage

`/register` create a new account.
Log in via `/login`.
`/profile` where information from the database is shown.
admin interface`/admin-login`  `admin`/`adminpassword`.

user1 user2 - demo users
