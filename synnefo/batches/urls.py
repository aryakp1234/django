from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about us'),
    path('contact',views.contact,name='contact us'),
   
   
]
