# Beat Server

[![Build Status](https://travis-ci.org/rajasimon/beatserver.svg?branch=master)](https://travis-ci.org/rajasimon/beatserver)

Beat Server is a scheduler, Periodic Tasks for Django channels | beta software


### Configurations

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

    beatserver django_project.asgi:channel_layer
