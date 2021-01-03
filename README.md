# Fluttalor-API

## Install

```pip install -r requirements.txt```

## Settings for localhost:

You need to uncomment :
- The environement setup (23 - 26) and fill it with your informations
- The DATABASES (124 - 129)

You need to comment ```django_heroku.settings(locals())``` at the end of the files.

You can uncomment the ```DEBUG = True``` if needed.