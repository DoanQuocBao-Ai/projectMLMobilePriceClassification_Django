from . import views
from django.urls import path

urlpatterns = [
        path('', views.index, name='index'),
        path('home', views.index, name='index'),
        path('train', views.train, name='train'),
        path('predict', views.predict, name='predict'),
        path('database', views.database, name='database'),
        path('tresult', views.tresult, name='tresult'),
        path('presult', views.presult, name='presult'),
]