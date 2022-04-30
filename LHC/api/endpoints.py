from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mainapp.models import bookings
from .serializers import ItemSerializer
@api_view(["POST"])
def add(request):
    serializer=ItemSerializer(data=request.data)
    j=1
    if serializer.is_valid():
        vd=serializer.validated_data
        details=bookings.objects.values().filter(Date=vd.get("Date"),Venue=vd.get("Venue"),Room=vd.get("Room"))
        for i in range(0,len(details)):
            if ((vd.get("Starttime")>details[i]["Starttime"] and vd.get("endtime")<details[i]["endtime"]) or (vd.get("Starttime")<details[i]["Starttime"] and vd.get("endtime")<details[i]["endtime"]) or (vd.get("Starttime")<details[i]["endtime"] and vd.get("endtime")>details[i]["endtime"])):
                j=0
    if j==1:
        serializer.save()
        return Response("Booking confirmed")
    else:
        return Response("Already booked")

    
@api_view(["GET"])
def existing(request):
    book=bookings.objects.all().values()
    serializers=ItemSerializer(book,many=True)
    return Response(serializers.data)
@api_view(["DELETE"])
def cancel(request):
    details=bookings.objects.get(id=1)
    if details:
        details.delete()
        return Response("Deleted")
    else:
        return Response("No existing booking")
    
    