# admaren_mt
mt data


Create an env and activate it

* virtualenv envs --python=python3.6

* pip install -r requirements.txt


I have commited migration files with used sqllite db in repo

tested user details : 
   username : tins
   password : swordfish

for fresh db : delete the "db.sqlite3" from folder and run,
 * python manage.py makemigrations
 * python manage.py migrate
 * python manage.py createsuperuser

## API details

1. Login API

    http://127.0.0.1:8000/api/token/
    
    {
    "username": "tins",
    "password": "swordfish"
    }

2. Refresh API
   http://127.0.0.1:8000/api/token/refresh/
   
## I have used **viewsets.ModelViewSet** to write APIs, so all the availabe rest methods will be registered with DefaultRouter with pagination and filter options

All APIS need to be authenticated 

## need to pass Authorization in header : sample token  
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NjYwMjExLCJqdGkiOiI5ZWZkMTY5ZDA1YjM0YTYzYmY5NjY4M2E0MDUzOWE5YiIsInVzZXJfaWQiOjF9.37HSmpzEFjd7y2T5US8AFlBOv9kWOodkpAHHIOrhZA8


3. Overview API

  http://127.0.0.1:8000/api/dashboard/
  
4. Crete API

   method : post
   
   http://127.0.0.1:8000/api/snippets/
   
   {
    "text": "tins k johny is the name",
    "tag": "title"
    }

5. Details API,
   method : get
   http://127.0.0.1:8000/api/snippets/id/ 
   
   (id is the primary key) 
   
6. Update API 
   method : patch or put (patch for updating only one data)
   
   http://127.0.0.1:8000/api/snippets/id/    
   
   (id is primary key)
   
   {
    "text": "tins k johny is the name",
    "tag": "title"
    }
    
7. Delete API

   method : delete
   
   http://127.0.0.1:8000/api/snippets/id/ 
   
   (id is primary key)
   
8. Tag list API
   method : get

   http://127.0.0.1:8000/api/tags/
   
   
9. Tag details
   method : get
   
   http://127.0.0.1:8000/api/tags/id/      (id is primary key)
