from django.urls import path
from . import views
# from rest_framework_jwt.views import (
#     obtain_jwt_token,
#     refresh_jwt_token,
#     verify_jwt_token,
#     )



urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='login'),
    # path('token/', obtain_jwt_token),
    # path("token/refresh/",refresh_jwt_token),
    # path("token/verify/",verify_jwt_token),

]