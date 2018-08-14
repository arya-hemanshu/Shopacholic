# Shopacholic
A dummy shopping app in flask 

# Requirements
- Mysql
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Script
- PyMySQL
- Python

# To run
- Clone the repo "git clone https://github.com/arya-hemanshu/Shopacholic.git"
- Change the Database User name and Password in "settings.py"
- Go to the folder in Terminal and follow these steps:
  - ```python initdb.py```
  - ```python manage.py db init```
  - ```python manage.py db migrate```
  - ```python manage.py db upgrade```
  - ```python init_db_records.py```
  - ```python manage.py server```
- The sever should start listening on http://localhost:5000

### Note: Make sure mysql is running

# To run tests
- Make sure mysql is running
- Go to the folder in Terminal and type ```python test_shopacholic.py```
