# Beat Server

[![Build Status](https://travis-ci.org/rajasimon/beatserver.svg?branch=master)](https://travis-ci.org/rajasimon/beatserver)
[![PyPI version](https://badge.fury.io/py/beatserver.svg)](https://badge.fury.io/py/beatserver)

Beatserver, a periodic task scheduler for django channels | beta software

### How to install

    pip install -U beatserver

### Configurations:

    Add `beatserver` to installed apps

    # beatconfig.py
    from datetime import timedelta

    BEAT_SCHEDULE = {
        'testing-print': {
            'type': 'test.print',
            'message': {'foo': 'bar'},
            'schedule': timedelta(seconds=5)
        },
    }

### How to run:

    python manage.py beatserver
