scrapy-notifications
====================

Send HTTP notifications on spider actions.

A Scrapy extension to be used, for example, with `HTTP Callback Tasks <http://docs.celeryproject.org/en/latest/userguide/remote-tasks.html>`_
of Celery project.

Installation
------------

Install via pip

.. code-block:: bash

    pip install scrapy-notifications

Setup
-----

Basically you need configure ``SPIDER_NOTIFICATION_ENABLED``,
``SPIDER_NOTIFICATION_URL`` and add the
``scrapy_notifications.extensions.SpiderNotification`` extension to your
Scrapy project ``settings.py``.

Example:

.. code-block:: python

    EXTENSIONS = {
        'scrapy_notifications.extensions.SpiderNotification': 500,
    }
    SPIDER_NOTIFICATION_ENABLED = True
    SPIDER_NOTIFICATION_URL = 'http://app.example.com/spider-task/'

By default HTTP requests are sent with the spider name attribute as an URL
parameter.
But optionally you can also specify a list of spider attributes passed as
URL parameters on ``SPIDER_NOTIFICATION_ATTRS``.

.. code-block:: python

    SPIDER_NOTIFICATION_ATTRS = ['name', 'jobid']

Usage
-----

For example crawling with the ``dmoz`` spider used in the
`Scrapy tutorial <https://scrapy.readthedocs.org/en/latest/intro/tutorial.html>`_

.. code-block:: bash

    scrapy crawl -a jobid=fe648c57f8 dmoz

will generate a HTTP request like this

.. code-block::

    http://app.example.com/spider-task/?name=dmoz&jobid=fe648c57f8

