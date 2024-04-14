from django.urls import path

from home.views import *

urlpatterns = [
    path('',IndexView.as_view(),name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Add other URLs as needed
]