<p align="center"><img src="logo/horizontalversions.png" alt="beatserver" height="150px"></p>

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
        'testing-print': [
            {
                'type': 'test.print',
                'message': {'testing': 'one'},
                'schedule': timedelta(seconds=5)  # Every 5 seconds
            },
            {
                'type': 'test.print',
                'message': {'testing': 'two'},
                'schedule': '0 3 * * 1'  # Precisely at 3AM on Monday
            },
        ]
    }

    Schedules can be specified as timedeltas for running tasks on specified intervals,
    or as cron-syntax strings for running tasks on exact schedules.

### How to run:

    python manage.py beatserver
