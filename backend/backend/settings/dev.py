from .common import *
INSTALLED_APPS += [  'debug_toolbar',]


MIDDLEWARE =[
    'debug_toolbar.middleware.DebugToolbarMiddleware',  #처음에추가
    ]+MIDDLEWARE

INTERNAL_IPS = ['127.0.0.1']
CORS_ORIGIN_WHITELIST =["http://localhost:3000"]
# CORS_ALLOWED_ORIGINS  =  [ 
#     "https://example.com" , 
#     "https://sub.example.com" , 
#     "http://localhost:8080" , 
#     "http://127.0.0.1:9000" , 
# ]