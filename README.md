# Wine shop
An online wine shop webapp powered by Django

## How to use

### 1. Inside *hackerearth_one* directory run the following command to install `pipenv`
```commandline
pip3 install pipenv
```
### 2. Activate `pipenv` virtual environment
```commandline
pipenv shell
```
### 3. Install packages
```commandline
pipenv install
```

### 4. Run database migrations (inside outer `wine_shop` directory)
```commandline
python manage.py migrate
```
### 5. Create superuser
```commandline
python manage.py createsuperuser
```
### 8. Run development server
```commandline
python manage.py runserver
```