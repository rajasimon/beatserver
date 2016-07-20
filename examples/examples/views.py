from random import randint
from channels import Channel
from django.http import HttpResponse


# Create your views here.
def home(request):
    number = randint(1, 343333333)
    Channel('hae-repeat-me').send(
        {
            'number': number,
            'status': True,
            'delay': 10
        }
    )
    return HttpResponse("testing")
