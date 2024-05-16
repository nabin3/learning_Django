# learning_Django
Sharing my Django journey with Sir [Hitesh Choudhary](https://www.linkedin.com/in/hiteshchoudhary/) from [Chai aur Django](https://youtube.com/playlist?list=PLu71SKxNbfoDOf-6vAcKmazT92uLnWAgy&si=pghcoCquTC_g3axO)

## Table of Contents
- [Setup_virtual-env](#setup_virtual-env)
- [Starting_Django_Project](#starting_django_project)

## Setup_virtual-env <a name="setup_virtual-env"></a>
I choose uv for managing packages and venv because it's faster.
```bash
pip install uv
```
and now crteating venv
```bash
uv venv
```
now I activate venv 
```bash
source .venv/bin/activate
```

## Starting_Django_Project <a name="starting_django_project"></a>
Installing Django inside virtual-environment(.venv)
```bash
uv pip install Django
```
Creating a django project, a django project is collection of settings and configurations that define the structure and behaviour of a web application.
It includes applicatio code, template, statiuc files and other resources that make up the application.
```bash
django-admin startproject chaiaurdjango # This will create a folder chaiaurdjango with basic structure of a Django project
cd chaiaurdjango
```
Starting a Django server
```bash
python manage.py runserver <port for listening> 
```
above command will deploy a server which will be listening on port :8000, by default it will listen on 8000, so we can ommit the port number.

Learnt about different level of a python project directory, like root level, project level, app level.