from .common import *
INSTALLED_APPS += [  'debug_toolbar',]


MIDDLEWARE =[
    'debug_toolbar.middleware.DebugToolbarMiddleware',  #처음에추가
    ]+MIDDLEWARE

INTERNAL_IPS = ['127.0.0.1']