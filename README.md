# blog0
Blog/update type application

## instilations
```
pip3 install flask
```

## requirements
```
Python 3.6.9
click==7.1.1
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
Werkzeug==1.0.1
```

## running localhost
```
- clone the repo
- cd into blog0
$ python3 flaskblog.py
- you can vist http://localhost:5000/
```

## working with virtualenv
```
Create virtualenv:
$ virtualenv env_name

Start virtualenv:
cd to directory just outside of desired environment
$ source env/bin/activate

export packages and their version numbers:
$ pip3 freeze --local > requirements.txt

import packages and their version numbers:
$ pip3 install -r requirements.txt

End virtualenv:
$ deactivate

Delete virtual environment:
$ rm -rf environment/

Create virtualenv with specific python:
$ virtualenv -p /user/bin/pythonX.X env_name
```

## problems
```
- should try deploy. Maybe using heroku
```
