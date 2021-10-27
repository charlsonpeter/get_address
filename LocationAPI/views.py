from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
from .models import *
# Create your views here.


class GetAddress(APIView):
    def get(self, request, lat, long):
        try:
            ins_loc = Locations.objects.filter(latitude=lat, longitude=long).last()
            if ins_loc and ins_loc.updated_at+timedelta(hours=24) >= datetime.now():
                return Response({'name':ins_loc.address})
            geolocator = Nominatim(user_agent="LocationApi")
            location = None
            try:
                location = geolocator.reverse(str(lat)+","+str(long))
                location = location.raw
                if ins_loc:
                    Locations.objects.filter(latitude=lat, longitude=long).update(updated_at=datetime.now())
                else:
                    Locations.objects.create(latitude=lat, longitude=long, address=location['display_name'], updated_at=datetime.now())
            except Exception as e:
                raise
            return Response({'name':location['display_name']})
        except Exception as e:
            return Response({'status':0,'reason':str(e)})
