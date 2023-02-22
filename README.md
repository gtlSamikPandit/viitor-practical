# viitor-practical

- Practical task for viitor cloud.

- User calories tracker application. Build using Python Django and Django REST Framework.

### Installation Guidelines:

- Clone the repository


- Create virtual environment at the directory where venv is already ignore at .gitignore file
    
    ```
    pip install virtualenv
    ```
  
    ```
    cd /to/project/directory
    ```
  
    ```
    virtualenv -p=python3.9 venv
    ```

- Activate the virtual environment & install requirements
    
    ```
    source /venv/bin/activate
    ```
  
    ```
    pip install -r requirements.txt
    ```

- Generate a local settings file `local.py` same as `resumex/settings/example-production.py`.


- Run the following command for database migrations:

    ```
    python manage.py makemigrations
    ```
  
    ```
    python manage.py migrate
    ```

- Run project with

    ```
    python manage.py runserver
    ```
  
### Project Overview:

- Project API docs link:

    ```
    http://127.0.0.1:8000/api/v1/docs/
    ```
  
- User Registration:

    ```
    http://127.0.0.1:8000/api/v1/user/registration/
  
    {
        "username": "jay",
        "password1": "Dummy@1234",
        "password2": "Dummy@1234",
        "email": "jay@dummy.com"
    }
    ```
  
- User Login:

    ```
    http://127.0.0.1:8000/api/v1/user/login/
  
    {
        "username": "jay",
        "password": "Dummy@1234"
    }
    ```
  
- Use the generated authentication token for all APIs.