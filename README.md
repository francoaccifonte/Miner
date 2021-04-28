# DsSandbox
Web Application that scraps the web for useful data.

## Setup
### MySQL
```
sudo apt-get install -y mysql-server
sudo apt install -y python3 libmysqlclient-dev default-libmysqlclient-dev
```
### Database
Run MySQL 
```
sudo mysql -u root
```
Then create the database and django credentials
```
CREATE DATABASE rusty_scrap;
CREATE USER 'firstuser'@'localhost' IDENTIFIED BY 'franco2019';
GRANT ALL ON rusty_scrap.* TO 'firstuser'@'localhost';
FLUSH PRIVILEGES;
```
### Python libs
```
python3 -m venv env/
source env/bin/activate
.\env\Scripts\Activate.ps1
pip install --upgrade setuptools
pip install ---upgrade pip
pip install wheel
pip3 install -r requirements.txt
deactivate
```
### Setting up the models
From MyFuture directory run
```
python manage.py migrate
```
## Running the App
From scrapApp directory run
```
scrapyd
```
From MyFuture directory run
```
python manage.py runserver
```