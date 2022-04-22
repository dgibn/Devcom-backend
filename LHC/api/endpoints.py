from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mainapp.models import bookings
from .serializers import ItemSerializer
@api_view(["POST"])
def add(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(["GET"])
def existing(request):
    book=bookings.objects.all().filter(Date__startswith="20")
    serializers=ItemSerializer(book,many=True)
    return Response(serializers.data)
@api_view(["DELETE"])
def cancel(self,request,EventName,Date,Time,format=None):
    details=bookings.objects.filter(EventName=EventName,Date=Date,Time=Time)
    if details:
        details.delete()
        return JsonResponse({"status":"ok"},status=status.HTTP_200_OK)
    return JsonResponse(ItemSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
    