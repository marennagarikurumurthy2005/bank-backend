from django.urls import path
from .views import Registrationview,Loginview,Dashboardview,Transactionview


urlpatterns = [
    path('register/',Registrationview.as_view()),
    path('login/',Loginview.as_view()),
    path('dashboard/',Dashboardview.as_view()),
    path('transaction/',Transactionview.as_view())
]
