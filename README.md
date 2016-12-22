## Django Tutorial
[![Build Status](https://travis-ci.org/henriquebraga/django-tutorial.svg?branch=master)](https://travis-ci.org/henriquebraga/django-tutorial)
[![Code Health](https://landscape.io/github/henriquebraga/django-tutorial/master/landscape.svg?style=flat)](https://landscape.io/github/henriquebraga/django-tutorial/master)g
Django tutorial from the official documentation.
(with some additional tests)

More in:

https://docs.djangoproject.com/en/1.10/intro/tutorial01/

## How to develop?

1. Clone the repository
2. Create a virtualenv with Python 3.5
3. Activate virtualenv
4. Install the dependencies
5. Execute tests.

```console
git clone git@github.com:henriquebraga/django-tutorial.git django-tutorial
cd django-tutorial
pytho -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```