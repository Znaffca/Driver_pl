# DRIVER_pl - portfolio_lab project <br>
Portfolio lab project - description in progress...

#### 25.02.2019 - what is working:
- in progress


#### To-Do-List:
 - in progress
 
#### Known issues:
- Donates Validation
- probably much more than that...

### Download and use it in your local environment:
- Fork repository
- Clone it into your computer
- Create virtualenv for the project, install requirements using: 
    ```sh
    $ pip install -r Requirements.txt
    ```
- create file `local_settings.py` with your local configuration:
 ```python
DATABASES = {
        'default': {
            'HOST': 'localhost',
            'NAME': 'your_db_name',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'username',
            'PASSWORD': 'password',
        }
    }
    

```
- create empty database in psql
- run `python manage.py makemigrations``python manage.py migrate`
- start test server.
### Enjoy :)
   