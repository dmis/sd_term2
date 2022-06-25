from time import sleep
from django.http import HttpResponse


def index(request):
    try:
        sleep(1)
    finally:
        return HttpResponse('{\'type\': \'django\'}')
