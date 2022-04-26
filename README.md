# Devcom-backend
The main project is named LHC__
The app name is mainapp__
The folder api consists of all the endpints api's created including the serializers as well as the urls and endpoints__
The database model where the data is stored is named "Bookings".__
The model stores the EventName,Venue which could be complex A,B,C, Room which is of the format "LT-101",the date of the booking "dd/mm/yyyy" and the time in military format "0000".
I installed the rest_framework and added to the installed apps as well as my mainapp.
I installed the django rest framework packages.
The endpoints are "newbookings" in order to add the data,"existing" in order to list the bookings on a particular date and "cancelbooking" in order to delete an existing booking.
I added the api.urls to the urls.py of the LHC project.
