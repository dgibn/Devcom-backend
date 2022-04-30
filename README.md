# Devcom-backend
The main project is named _**LHC**_ <br>
The app name is _**mainapp**_<br>
The folder api consists of all the endpints api's created including the serializers as well as the urls and endpoints<br>
The database model where the data is stored is named "**Bookings**".<br>
The model stores the following:<br> EventName<br>Venue which could be complex A,B,C<br>Room which is of the format "LT-101"<br>the date of the booking "dd/mm/yyyy" <br>Starttime is of type TimeField which stores the start time of the event in 24 hr format.<br>Endtime is of type TimeField which stores the end time of the event in 24 hr format.<br>
I installed the rest_framework and added to the installed apps as well as my mainapp. <br>
I installed the django rest framework packages.<br>
The endpoints are:
<br>"newbookings" in order to add the data<br>"existing" in order to list the bookings on a particular date <br>"cancelbooking" in order to delete an existing booking.Write now I have added the fucntion that if you delete in the "cancelbooking" endpoint it deletes the data with id=1.
<br>
