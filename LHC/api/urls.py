from django.urls import path
from . import endpoints
urlpatterns=[path("newbooking",endpoints.add),path("existing",endpoints.existing),path("cancelbooking",endpoints.cancel),]

