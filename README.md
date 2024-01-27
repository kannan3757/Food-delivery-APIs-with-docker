## Prerequisites:
* Python 3.8.10 is installed and preferred to have a virtual environment.
* Required postgreSQL server access or installed on your local.

## One time Setup:
1. Activate the virtual environment
2. Ignore if the virtual environment had already installed the required packages, otherwise install the python library packages specified in the requirement.txt using the command `$ pip install requirement.txt`
3. Create a database in postgreSQL server and provide the access for a specific user `$ su - postgres; createuser productmanagementuser; psql; ALTER USER productmanagementuser WITH ENCRYPTED password '<Thbs123!>'; CREATE DATABASE productmanagementdb OWNER productmanagementuser; GRANT ALL PRIVILEGES ON DATABASE productmanagementdb to productmanagementuser;`
4. Define proper database and log configuration from the files <Project_Home>/config/database.json

## Run application
1. Any code changes - pull from the branch to local
2. Execute the database migrations using `$ python manage.py makemigrations; python manage.py migrate; python manage.py collectstatic;`
3. Run the application `$ python manage.py runserver 127.0.0.1:4010`


