# Beat Server

Beat Server is a scheduler, Periodic Tasks for Django channels | beta software


### Configurations

    # beatconfig.py
    from datetime import timedelta

    BEAT_SCHEDULE = {
        'add-every-10-seconds': {
            'channel_name': 'testing',
            'schedule': timedelta(seconds=30),
            'message': {'foo': 'bar'}
        },
    }

### How to run:

    beatserver django_project.asgi:channel_layer
