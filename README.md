# Beat Server

[![Build Status](https://travis-ci.org/rajasimon/beatserver.svg?branch=master)](https://travis-ci.org/rajasimon/beatserver)
[![PyPI version](https://badge.fury.io/py/beatserver.svg)](https://badge.fury.io/py/beatserver)

Beatserver, a periodic task scheduler for django channels | beta software

### How to install

    pip install -U beatserver

### Configurations:

    # beatconfig.py
    import os
    from datetime import timedelta
    from channels.layers import get_channel_layer
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alamo_projects.settings")
    channel_layers = get_channel_layer()
    
    BEAT_SCHEDULE = {
        'add-every-10-seconds': {
            'channel_name': 'testing',
            'schedule': timedelta(seconds=10),
            'message': {'foo': 'bar'}
        },
    }

### How to run:

    beatserver django_project.beatconfig:application
