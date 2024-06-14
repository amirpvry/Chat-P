from django.urls import path
from APPSAMPLE.views import *
app_name = 'appsample'
urlpatterns = [

    path('', index, name= 'home' ),
    path('about',about, name = "about" ),
    path('contact', contact_view , name= 'contact'),
    path('test', test, name='test')
    
]
