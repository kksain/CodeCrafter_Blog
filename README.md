### Create Virtual Environment
python -m venv myvirtualenv

### Activate virtual environment
myvirtualenv\Scripts\activate

## Clone the repository:
- git clone https://github.com/kksain/CodeCrafter_Blog.git

## Navigate to the project directory:
- cd CodeCrafter_Blog

### Install dependencies:
pip install -r requirements.txt

### Apply database migrations:
python manage.py migrate

## Run the development server:
- python manage.py runserver

## Access the application at http://localhost:8000/.
