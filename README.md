### Create Virtual Environment
python -m venv myvirtualenv

### Activate virtual environment
myvirtualenv\Scripts\activate

### Start Project
django-admin startproject CodeCrafter

### Install Requirement
pip install -r requirements.txt


### Migration
python manage.py migrate

### Create Superuser
python manage.py createsuperuser