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
        'add-every-10-seconds': {
            'channel_name': 'testing',
            'schedule': timedelta(seconds=10),
            'message': {'foo': 'bar'}
        },
    }

### How to run:

    python manage.py beatserver
