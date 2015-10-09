# django-suit-rq

> Support for the django-rq admin when using django-suit

[![Latest Version](https://img.shields.io/pypi/v/django-suit-rq.svg?style=flat)](https://pypi.python.org/pypi/django-suit-rq/)

[Django-rq](https://github.com/ui/django-rq) already provides a nice admin interface, but it doesn't look good with [django-suit](http://djangosuit.com/). This fixes that.

## Quick start

1. Install the package from pypi:

    ```bash
    pip install django-suit-rq
    ```

2. Add "suit_rq" your INSTALLED_APPS. This needs to be added **before** `django_rq`:

    ```python
    INSTALLED_APPS = (
        'suit',
        'suit_rq',
        'django_rq',
    )
    ```
