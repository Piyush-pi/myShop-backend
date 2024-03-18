# myShop-backend
The goal is to create a Web application using Django framework to Recommend Products to the User on ECommerce Shop as per their Search

#### Getting Started

Project Setup [Installation Steps]

Install virtual environment

```

pip install virtualenv

```

create and activate the virtual env

```

python3 -m venv "venv_name"

source venv/bin/activate

```

Install requirements 

```
pip install -r requirements.txt
```

Migrate 

```

python manage.py migrate

```

Run 

```

python manage.py runserver

```

#### Setup Django Admin (optional)
NOTE: if you do not want to create superuser you can skip this step
Run 
```
python manage.py createsuperuser

```

#### Use Below command to create 2 users from fixture
Run 
```
python manage.py loaddata fixtures/users.json
```

#### Use Below command to create 10000 products using command
Run 
```
python3 manage.py create_random_products
```

#### Swagger DOCS URL

[http://localhost:8000/swagger/](http://localhost:8000/swagger/)