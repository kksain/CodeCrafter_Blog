### Create Virtual Environment
python -m venv myvirtualenv

### Activate virtual environment
myvirtualenv\Scripts\activate

### Install Requirement
pip install -r requirements.txt

### Start Project
django-admin startproject CodeCrafter

### Migration
python manage.py migrate

### Create Superuser
python manage.py createsuperuser