# Create a virtual environment
python -m venv asset_tracker_env
asset_tracker_env\Scripts\activate  # for Windows

# Install Django
pip install django

# Create a new Django project
django-admin startproject asset_tracker
cd asset_tracker

# Create a new Django app
python manage.py startapp asset_management
