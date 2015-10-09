django-suit-rq
==============

Support for the django-rq admin when using django-suit

Quick Start
-----------

1. Install the package from pypi:

    .. code-block:: bash

        pip install django-suit-rq

2. Add "suit_rq" your INSTALLED_APPS. This needs to be added _before_ `django_rq`:

    .. code-block:: python

        INSTALLED_APPS = (
            'suit',
            'suit_rq',
            'django_rq',
        )
