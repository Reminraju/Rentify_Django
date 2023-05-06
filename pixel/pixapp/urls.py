from . import views
from django.urls import path
urlpatterns=[
    path('',views.geg,name="geg"),
    path('re',views.ger,name="ger"),
    path('we',views.ter,name="ter"),
    path('login',views.log,name="log"),
    path('xe',views.contact,name="con"),
    path('ce',views.abo,name="abo"),
    path('main/',views.hed,name="hed"),
    path('booking',views.book,name="book")
]