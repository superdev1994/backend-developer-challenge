import json

from django.contrib.auth.models import User, Group

from django.http import Http404, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core import serializers

from rest_framework import viewsets, generics, permissions, decorators

from .serializers import UserSerializer, GroupSerializer, AirportSerializer
from .models import Airport
from .utils import calc_distance_between


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AirportViewset(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [permissions.AllowAny]

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    @decorators.action(methods=['get'], detail=False)
    def find_in_radius(self, request):
        queryset = Airport.objects.all()
        lat = request.GET['lat']
        lon = request.GET['lon']
        radius = request.GET['radius']

        if lat is not None and lon is not None and radius is not None:
            lat = float(lat)
            lon = float(lon)
            radius = float(radius)

            def filter_by_distance(airport):
                dist = calc_distance_between(
                    lat, lon, airport.latitude, airport.longitude)
                if (dist <= radius):
                    return True
                else:
                    return False

            queryset = filter(filter_by_distance, queryset)

            tmpJson = serializers.serialize("json", queryset)
            tmpObj = json.loads(tmpJson)

            return HttpResponse(json.dumps(tmpObj))
        else:
            raise Http404
