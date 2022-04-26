# Devcom-backend
The main project is named _**LHC**_ <br>
The app name is _**mainapp**_<br>
The folder api consists of all the endpints api's created including the serializers as well as the urls and endpoints<br>
The database model where the data is stored is named "**Bookings**".<br>
The model stores the following:<br> EventName<br>Venue which could be complex A,B,C<br>Room which is of the format "LT-101"<br>the date of the booking "dd/mm/yyyy" <br>Starttime in military format "0000".<br>Endtime in military format "0000".<br>
I installed the rest_framework and added to the installed apps as well as my mainapp. <br>
I installed the django rest framework packages.<br>
The endpoints are:
<br>"newbookings" in order to add the data<br>"existing" in order to list the bookings on a particular date <br>"cancelbooking" in order to delete an existing booking.
<br>I added the api.urls to the urls.py of the LHC project.
